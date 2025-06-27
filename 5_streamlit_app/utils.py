import os
import uuid


#What ever the file (imgae / video ) we are uploding in stream lit , those images will be saved here

def handle_upload(uploaded_file):
    upload_dir = "5_streamlit_app/uploads"
    os.makedirs(upload_dir, exist_ok=True)  # Create folder if it doesn't exist

    # Generate a unique filename to avoid conflicts
    ext = os.path.splitext(uploaded_file.name)[-1]
    unique_name = f"{uuid.uuid4().hex}{ext}"

    file_path = os.path.join(upload_dir, unique_name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path  # Return the saved file path

