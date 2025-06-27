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

### 🤖 Phase 5: LLM Chatbot (LangChain + SQL Agent)
- Enable natural language querying of compliance and violation data stored in RDS using a LangChain-powered chatbot.

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
