# ===== IMPORTS =====
import os
import sys
import cv2
import time
import streamlit as st
import numpy as np
import json
import pandas as pd
from ppe_detection import detect_objects
from utils import handle_upload



# ===== SETUP =====
st.set_page_config(page_title="Intelliguard PPE Compliance", layout="wide")

#Back Ground COlor:
st.markdown( """<style> .stApp {background-color: #fafcd2;}</style>""",unsafe_allow_html=True)

#Title
st.markdown("<h1 style='text-align: center;'>🛡️ Intelliguard PPE Detection System</h1>",unsafe_allow_html=True)



## ===== AUTHENTICATION SETUP =====
#Import Auth Paths
from auth_path import  setup_auth_paths
face_recognition_path = setup_auth_paths()




## ✅ Import face recognition functions
from face_Login import recognize_face_login as run_face_login
from face_detect import face_detected as face_detect  # if it exists
from face_registration import save_uploaded_face as run_face_register

# ✅ Import PIN-based functions
from login_user import login_user as run_login_user
from register_user import register_user as run_register_user

#✅ Import S3 Bucket
from s3bucket_File_uploader import upload_file_to_s3 as run_s3_bucket


#✅ Import AWS Integration - Postgresql - Logs
from log_violation import log_violation_to_rds as run_log_violation_to_rds

#✅ Import Chatbot path
# from LLM_SQL_agent import run_chat_query as run_chat_query

from ollama_query import run_ollama_query as run_ollama_query


#Import Emial Path:
from emailer import send_violation_email as send_violation_email

## ===== AUTHENTICATION SETUP =====


# ===== LOGIN INTERFACE =====
def login_interface():
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("🔐 Login to Intelliguard")
    st.markdown("<br>", unsafe_allow_html=True)

    auth_choice = st.radio("Select Authentication Action", [
        "Face Login",
        "Face Register",
        "PIN Login",
        "PIN Register"
    ])
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Face Login ---
    #It will not show face in streamlit
    # if auth_choice == "Face Login":
    #     if st.button("🔍 Authenticate with Face"):
    #         if run_face_login():
    #             st.success("✅ Face recognized! Login successful.")
    #             st.session_state.authenticated = True
    #         else:
    #             st.error("❌ Face not recognized.")
    
    #it will show face in streamlit
    if auth_choice == "Face Login":
        if st.button("🔍 Authenticate with Face"):
            try:
                name, face_img = run_face_login()
                if name:
                    st.session_state.authenticated = True
                    st.session_state.auth_name = name
                    st.session_state.face_img = face_img

                    face_img_rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
                    st.image(face_img_rgb, caption=f"Authenticated Face: {name}", width=300)
                    st.success(f"✅ Welcome, {name} (Face Authenticated)")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("❌ Face not recognized.")
            except Exception as e:
                st.error(f"⚠️ Face recognition failed: {e}")


    elif auth_choice == "Face Register":
        username = st.text_input("👤 Enter a username to register")
        st.markdown("<br>", unsafe_allow_html=True)
        
        choice = st.radio("Choose image input method", ["Capture from Webcam", "Upload Image File"])
        st.markdown("<br>", unsafe_allow_html=True)

        if choice == "Capture from Webcam":
            st.warning("📸 Webcam capture via Streamlit is not supported directly.")
            st.markdown("➡️ Please run the standalone script if webcam capture is needed.")

        elif choice == "Upload Image File":
            uploaded_file = st.file_uploader("📂 Upload a face image", type=["jpg", "jpeg", "png"])
        st.markdown("<br>", unsafe_allow_html=True)    

        if st.button("📝 Register New Face") and username:
            if choice == "Upload Image File" and uploaded_file:
                st.info("✅ File uploaded...")
                # Prepare save path
                save_dir = os.path.join(face_recognition_path, "known_faces_images", username)
                os.makedirs(save_dir, exist_ok=True)

                # Decode image
                file_bytes = uploaded_file.read() #returns a byte stream  of the image file — not an actual image 
                img_array = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR) #To convert this byte stream into an image array that OpenCV (cv2) can work with. must decode it into a NumPy array.     
                #np.frombuffer(file_bytes, np.uint8) ->  >>> np.frombuffer(b'\xff\xd8\xff\xe0...', np.uint8)  ->  array([255, 216, 255, 224, ...], dtype=uint8) -> it convert into NumPy array which is 1D

                # cv2.imdecode() -> is  OpenCV function that decodes the raw image byte array into a full image (like reading it from a file).
                #cv2.IMREAD_COLOR -> tells OpenCV to load the image in color mode (as BGR: Blue, Green, Red). #3D
                # Now, the result is a standard OpenCV image (i.e., a NumPy array of shape [height, width, 3]).


                if img_array is not None:
                    # Save face image
                    run_face_register(username, img_array)
                    st.image(img_array, caption="📸 Uploaded Face Preview", width=250)
                    st.success(f"✅ Face image saved for user '{username}'")

                    # Run face detection on this user's folder only
                    user_path = os.path.join(face_recognition_path, "known_faces_images", username)
                    st.info("🔎 Verifying face detection...")

                    st.image(img_array, caption="🧪 Image sent for detection", width=250)
                    cv2.imwrite("5_streamlit_App\debug_face.jpg", img_array)  # Local debugging if running locally


                    try:
                         detected = face_detect(user_path)  # You can modify face_detect() to return True/False
                         if detected:
                               st.success("✅ Face detection successful.")
                               st.session_state.authenticated = True
                               st.session_state.auth_name = username
                               st.session_state.face_img = img_array
                               time.sleep(5)
                               st.rerun()  # ⬅️ This is what brings you back into the 'else' block
                         else:
                              st.warning("⚠️ No face detected. Please try another image.")
                    except Exception as e:
                       st.error(f"❌ Face detection failed: {e}")

                else:
                    st.error("❌ Failed to decode the uploaded image. Please try a different file.")
                
            elif choice == "Upload Image File":
                st.error("⚠️ Please upload an image before registering.")







      # --- PIN Login ---
    elif auth_choice == "PIN Login":
        username = st.text_input("👤 Username", placeholder="Enter your name here")
        if username.strip():  # Ensures it's not empty or just spaces
            st.write(f"Username Entered: {username}")
        print("UserName Entered: ",username)


        password = st.text_input("PIN/Password", type="password", placeholder="Enter your Password/Pin here")
        print("Password Entered: ",password)
        # st.write("Password Entered: ",password)

        if st.button("🔐 Login"):
            if run_login_user(username, password):
                st.success(f"{username} ✅ Login successful.")
                st.session_state.authenticated = True
                st.session_state.auth_name = username
                time.sleep(5)
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")




    # --- PIN Register ---
    elif auth_choice == "PIN Register":
        username = st.text_input("Choose 👤Username", placeholder="Enter your name here")
        if username.strip():  # Ensures it's not empty or just spaces
            st.write(f"Username Entered: {username}")
        print("UserName Entered: ",username)

        pin = st.text_input("Choose a PIN/Password", type="password", placeholder="Enter your Password/Pin here")
        print("Password Entered: ",pin)
        # st.write("Password Entered: ",pin)

        if st.button("🧾 Register"):
            success, msg = run_register_user(username, pin)
            if success:
              st.success(msg)
              st.session_state.authenticated = True
              st.session_state.auth_name = username
              time.sleep(2)
              st.rerun()
            else:
              st.error(msg)
# ===== LOGIN INTERFACE =====




# ===== MAIN APP FLOW =====
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login_interface()
else:
    st.success(f"✅ Logged in as {st.session_state.get('auth_name', 'User')}")

    if "face_img" in st.session_state and st.session_state.face_img is not None:
        st.image(
            cv2.cvtColor(st.session_state.face_img, cv2.COLOR_BGR2RGB),
            caption=f"Authenticated Face: {st.session_state.auth_name}",
            width=300
        )
    st.markdown("<br>", unsafe_allow_html=True)



    if "file_uploader_key" not in st.session_state:
        st.session_state.file_uploader_key = str(time.time())


    uploaded_file = st.file_uploader("📤 Upload an image or video", type=["jpg", "jpeg", "png", "mp4"],
                                     key=st.session_state.file_uploader_key)
    st.markdown("<br>", unsafe_allow_html=True)

    if uploaded_file:
        input_path = handle_upload(uploaded_file)
        result_path, violations, missing_items, positives, violations_conf_score,detected_items,no_of_violation_class = detect_objects(input_path)
        # violations_conf_score_json = json.dumps(confidence)

         # === Show result preview
        if result_path.endswith((".jpg", ".png")):
            st.image(result_path, caption="🖼️ Detection Output",width = 350 ) #use_container_width=True
        elif result_path.endswith(".mp4"):
            st.video(result_path)
        
        st.markdown("<br>", unsafe_allow_html=True)



    # === S3 Upload
    st.subheader("📤 Uploading detection result to AWS S3 Bucket...")
    print("\n","Detected/Predicted Image Path: ",os.path.basename(result_path))

    filename_on_s3 = f"uploaded_results/{os.path.basename(result_path)}"
    print("File Name on S3 Bucket: ",filename_on_s3)

    s3_url = run_s3_bucket(result_path, filename_on_s3)
    print("S3 URL: ",s3_url,"\n")

    if s3_url:
            st.success("✅ Uploaded to S3")
            st.markdown(f"[🔗 View Uploaded File on S3]({s3_url})")
    else:
            st.error("❌ Failed to upload to S3")

    # === RDS 
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Logging violations in AWS RDS...")
    image_url = s3_url
    all_violations_detected = ', '.join(violations | missing_items)
    run_log_violation_to_rds(image_url, detected_items,no_of_violation_class, violations_conf_score)
    print("Uploaded the details to AWS RDS (postgres SQl DB)")
    st.success("✅ Uploaded to AWS RDS")
    st.markdown("<br>", unsafe_allow_html=True)



    st.subheader("📋 Detection Summary")
    if all_violations_detected:
            print(all_violations_detected)
            st.error(f"🚨 All Violations Detected: {all_violations_detected}")
    else:
            st.success("✅ All required PPE detected.")
    if positives:
            st.info(f"🟢 Compliant PPE Detected: {', '.join(positives)}")
    else:
            st.warning("⚠️ No compliant PPE detected.")
    st.markdown("<br>", unsafe_allow_html=True)
        
        
    st.subheader("📋 Log Violations Summary")
    st.info(f"[🔗 View Uploaded File on S3]({image_url})")
    st.info(f"Total Unique items detected in image: {detected_items}")
    st.info(f"🚨 Violations Detected in image:{no_of_violation_class}")
    st.info(f"Confidence Scores of Violations Detected in image: {violations_conf_score}")


    # Download log as CSV 
    with st.expander("📊 View Logs & Export"):
        df_logs = run_log_violation_to_rds(image_url, detected_items,no_of_violation_class, violations_conf_score)
        if df_logs is not None:
              st.dataframe(df_logs)
              st.download_button("Download Logs", df_logs.to_csv(index=False).encode(), file_name="violations.csv", mime="text/csv")
        else:
              st.warning("⚠️ No logs found or error occurred while fetching logs.")


    #Ask question to AI 
    st.title("💬 Ask About PPE Violations")
    query = st.text_input("Ask a question about the violation logs:")
        
    if st.button("Submit") and query:    

        log_summary = (df_logs.to_string(index=False) if df_logs is not None else "No logs available.")

        prompt = f"""You are an AI assistant helping with PPE compliance logs.
            Detection summary:
            Image URL: {image_url}
            Detected Items: {detected_items}
            Violations Detected: {no_of_violation_class}
            Confidence Scores: {violations_conf_score}
            Logs:{log_summary}
            
            User question: {query}
            Please provide a clear, helpful answer based only on this information."""

        # result = run_chat_query(prompt) #langchain
        result =run_ollama_query(prompt) #llama3.2:latest model
        st.markdown("### 📊 Response:")
        st.write(result)



    # Email
    st.title("Email Alerts")
    THRESHOLD = 1
            
    if len(no_of_violation_class) >= THRESHOLD:        
            # Compose email
                subject = "🚨 PPE Violations Alert"
                body = f"""Alert: {len(no_of_violation_class)} violations detected.
                Image URL: {image_url}
                Detected Items: {detected_items}
                Confidence Scores: {violations_conf_score}
                Please review immediately."""

                to_emails_input = st.text_input("Recipient Email IDs (comma-separated)",placeholder="e.g., abc@example.com, def@example.com")
                print("To Emails Entered:",to_emails_input)

                # Add a "Send Email" button
                if st.button("Send Email Alert"):
                    if to_emails_input.strip():  # Ensure not empty
                       
                        # to_emails=["bdharshini61997@gmail.com","dharshini61997@gmail.com"]  
                       # Split by comma and strip spaces
                        # to_emails = [email.strip() for email in to_emails_input.split(",") if email.strip()]

                       cleaned_to_emails = []
                       for email in to_emails_input.split(","):
                           cleaned_email = email.strip()
                           if cleaned_email:
                               cleaned_to_emails.append(cleaned_email)

            
                       # Debug output
                       print("To Emails:", cleaned_to_emails)
            
                       # Send email
                       send_violation_email(
                        subject=subject,
                        body=body,
                        to_emails=cleaned_to_emails)

                       # Show success warning
                       st.warning("📧 Auto-email alert sent to Safety Team.")
                    else:
                       st.error("Please enter at least one valid email address.")

    


# ===== LOGOUT =====
if st.button("🔓 Logout"):
    keys_to_clear = [
        "authenticated", "auth_name", "face_img",
        "uploaded_file", "image_path", "detections",
        "s3_url", "violation_classes", "confidence_scores",
        "predicted_image", "results", "file_name"
    ]
    for key in keys_to_clear:
        st.session_state.pop(key, None)
    
    # 🔄 Reset file_uploader widget by updating its key
    st.session_state["file_uploader_key"] = str(time.time())


    st.info("🔓 Logged out successfully.")
    time.sleep(2)
    st.rerun()

# ===== MAIN APP FLOW =====