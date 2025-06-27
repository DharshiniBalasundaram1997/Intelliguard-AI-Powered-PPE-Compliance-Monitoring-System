import cv2
import os
import numpy as np


# Base path where all face images are stored
BASE_DIR = "C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Final Project - 1/Project6_Code/Intelliguard_PPE_Detection/4_authentication/face_Recognition/known_faces_images"
print("Registering Face User in known images path: ",BASE_DIR,"\n")

#This function can be executed here only i.e. it can be executed in face_registration.py. testing purpose
def register_face_user_using_file_upload():
    """
    File uploaded face image to the user's directory(known images folder).
    """
    username = input("Enter username to register face: ").strip()
    print(username)
    
    save_dir = os.path.join(BASE_DIR, username)
    print("Path: ", save_dir)

    os.makedirs(save_dir, exist_ok=True)

    img_count = 0
    file_path = input("📂 Enter the full path to the image file: ").strip()
    if os.path.isfile(file_path):
            img = cv2.imread(file_path)
            if img is not None:
                img_path = os.path.join(save_dir, f"{username}_{img_count}.jpg")
                cv2.imwrite(img_path, img)
                print(f"✅ Saved uploaded image as: {img_path}")
            else:
                print("❌ Failed to read the selected image.")
    else:
            print("⚠️ File does not exist.")




#For streamlit purpose
def save_uploaded_face(username, img_array):
    print("UserName -> ",username)
    """
    Save an uploaded or webcam-captured face image to the user's directory(known images folder).
    """
    save_dir = os.path.join(BASE_DIR, username)
    os.makedirs(save_dir, exist_ok=True)

    # Count existing images to avoid overwrite
    #Verifying existing images:
    existing_images = []
    for f in os.listdir(save_dir): #eg: ['Sara_0.jpg']
        if f.endswith((".jpg", ".jpeg", ".png")):
            existing_images.append(f)
    print("Existing Image: ",existing_images)
    
    img_count = len(existing_images)
    print("Image Count: ",img_count)

    # Save new image
    img_path = os.path.join(save_dir, f"{username}_{img_count}.jpg")
    print(img_path) #Eg: C....known_faces_images/Sara/Sara_1.jpg

    success = cv2.imwrite(img_path, img_array)
    print(success)

    if success:
        return img_path
    else:
        raise Exception("Failed to save image.")

# Optional legacy function (CLI only)
def capture_face_from_webcam(username):
    """
    Capture face images via webcam (for standalone script use only).(known images folder).
    """
    save_dir = os.path.join(BASE_DIR, username)
    os.makedirs(save_dir, exist_ok=True)
    img_count = 0

    cap = cv2.VideoCapture(0)
    print("📸 Press 's' to save your face image. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Register Face", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            img_path = os.path.join(save_dir, f"{username}_{img_count}.jpg")
            cv2.imwrite(img_path, frame)
            print(f"✅ Saved: {img_path}")
            img_count += 1
        elif key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# username = input("Enter username to register face: ").strip()
# print(username)
# capture_face_from_webcam(username)

# Optional: enable standalone running
if __name__ == "__main__":
    register_face_user_using_file_upload()

    #With if __name__ == "__main__", the test code only runs when you directly execute log_violation.py (e.g., via terminal), not when imported by Streamlit.