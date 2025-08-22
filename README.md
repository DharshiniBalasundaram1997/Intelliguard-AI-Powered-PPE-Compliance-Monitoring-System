# 🚀 Intelliguard: AI-Powered PPE Compliance Monitoring System

A computer vision–powered object detection platform to monitor Personal Protective Equipment (PPE) compliance in manufacturing and industrial environments.

---

## 🛠️ Project Phases

### 🔬 Phase 1: Model Training & Core Object Detection
- Prepare and preprocess the dataset.
- Train and validate a YOLO-based object detection model to identify PPE compliance and violations.

### 🔐 Phase 2: Face/PIN Authentication
- Implement a face recognition module for secure user login.
- Provide an optional PIN/password fallback authentication mechanism.

### 🖥️ Phase 3: Streamlit App
- Develop a user-friendly Streamlit web application.
- Workflow: **Login → Upload image/video → Display detection results with bounding boxes.**

### ☁️ Phase 4: AWS Integration
- Store uploaded images/videos in AWS S3.
- Log violation metadata and detailed records to AWS RDS for analysis and reporting.

### 🤖 Phase 5: LLM Chatbot (Ollama3.2 Latest)
- Enable natural language querying of compliance and violation data stored in RDS using a llama-powered chatbot.

### 📧 Phase 6: Automation & Reporting
- Send automated email alerts when violations exceed predefined thresholds.
- Support CSV export of logged compliance data for audits and reports.

---

## ✅ Key Features
- Real-time object detection of PPE compliance.
- Secure authentication (Face ID and PIN/password).
- Cloud storage and structured database logging.
- Conversational AI interface for querying violations.
- Automated notifications and reporting tools.

---

## 📂 Project Structure
    Below is my current folder structure
    Intelliguard_PPE_Detection/
    │
    ├── 1_import_dataset.ipynb
    ├── 2_yolov8_model.ipynb
    ├── requirements.txt
    ├── yolov8n.pt
    ├── intelliguard-env
    ├── PPE_Images_dataset/
    │   ├── test
    │   │   ├── images
    │   │   ├── labels
    │   ├── train
    │   │   ├── images
    │   │   ├── labels
    │   ├── valid
    │   │   ├── images
    │   │   ├── labels
    ├── dlib
    ├── 4_authentication/
    │   └── face_recognition/
    │       ├── face_detect
    │       ├── face_Login.py     # Face recognition login
    │       ├── face_register.py      # Face registration
    │       ├── known_faces_images/
    │           ├── Dharshini
    │               ├── Dharshini_0.jpg
    │           ├── Rock
    │               ├── Rock_0.jpg
    │           ├── Sara
    │               ├── Sara_0.jpg
    │   └── pin_login/
    │       ├── login_user.py
    │       ├── register_user.py
    │       └── credentials.toml
    │   └── main_auth.ipynb
    │   └── path.py
    ├── ppe_training/
    │   └── ppe_compliance_model/
    │   │   └── weights
    │   │   │   └── best.pt
    │   │   │   └── last.pt
    │   │   └── args.yaml
    │   │   └── confusion_matrix_normalized.png
    │   │   └── confusion_matrix.png
    │   │   └── F1_curve.png
    │   │   └── labels_correlogram.jpg
    │   │   └── labels.jpg
    │   │   └── P_curve.png
    │   │   └── PR_curve.png
    │   │   └── R_curve.png
    │   │   └── results.csv
    │   │   └── results.png
    │   │   └── train_batch0.jpg
    │   │   └── train_batch1.jpg
    │   │   └── train_batch2.jpg
    │   │   └── val_batch0_labels.jpg
    │   │   └── val_batch0_pred.jpg
    │   │   └── val_batch1_labels.jpg
    │   │   └── val_batch1_pred.jpg
    │   │   └── val_batch2_labels.jpg
    │   │   └── val_batch2_pred.jpg
    ├── runs/
    │   └── detect/
    │   │   └── predict3/
    │   │   │   └── 15h_img_263_jpg.rf.322a8288620372c00832997189849870.jpg
    │   │   │   └── packing958_jpg.rf.2d9e1e0fed8d49d75115713c279f3a84.jpg
    │   │   │   └── packing991_jpg.rf.f9526c9cf9709bad10cd4ba9c21474fb.jpg
    ├── 5_streamlit_app/
    │   ├── streamlit_main.py                   # Main Streamlit app
    │   ├── auth_path.py         
    │   ├── ppe_detection.py             # Detection logic (YOLOv8 inference)
    │   ├── utils.py                 # Helper functions (image/video handling)
    │   ├── uploads/
    ├── AWS_Integration_6/
    │   ├── s3bucket_File_uploader.py
    │   └── cred.env
    │   └── rootkey.csv
    │   └── write_env_from_excel.py
    ├── database_7
    │   ├── aws_rds_cred.env
    │   ├── connect_rds_util.py
    │   ├── create_violation_table.py
    │   ├── log_violation.py
    ├── chatbot_8
    │   ├── ollama_query.py
    │   ├── LLM_SQL_agent.py
    │   ├── open_ai_cred.env
    ├── email_9
    │   ├── email_cred.env
    │   ├── emailer.py




## Streamlit Output:
![Main_Page-pin_login](https://github.com/user-attachments/assets/5564eaea-cf6d-410f-bc53-92fd96ad4a58)
![Main_Page-Pin_Register](https://github.com/user-attachments/assets/1b9beff6-596f-4c77-8b4e-c09610148427)
![Main_Page-Face_Register](https://github.com/user-attachments/assets/86a0c715-32ea-4587-9a82-1a47590695a5)
![Main Page - Face_Login](https://github.com/user-attachments/assets/99887912-69c0-4bc5-a051-0f7153293c1d)
![Main Page - Face_Login1](https://github.com/user-attachments/assets/56eaa271-1cba-4208-928e-e8eda0fab0c1)
![Second_Page1](https://github.com/user-attachments/assets/97049077-3dbf-401c-8317-f159948d1476)
![Second_Page_2](https://github.com/user-attachments/assets/4a439527-fe31-42ea-afba-84eeb0ad73b2)
![Second_Page_3](https://github.com/user-attachments/assets/320a6201-7494-47fb-9af4-3331d90d601c)
![Second_Page_4](https://github.com/user-attachments/assets/1bc7fa8d-a801-4e52-98c7-06a3993b947c)
![Download_csv_5](https://github.com/user-attachments/assets/f986f880-0e3c-4afd-bf8c-b36f013801a3)
![Chat_Bot](https://github.com/user-attachments/assets/36ede75a-9dae-4105-b3a9-fae4d0e40c8c)
![Email_Alerts_6](https://github.com/user-attachments/assets/2c8537b4-d6b2-4d5a-8aa8-f7f4a1c84d61)
![Email_Alerts_7](https://github.com/user-attachments/assets/3ee1be83-215d-40af-9f36-344b7f6756f8)
![email_7](https://github.com/user-attachments/assets/8f1f02af-d423-498c-bbbd-aa3bd543d688)












