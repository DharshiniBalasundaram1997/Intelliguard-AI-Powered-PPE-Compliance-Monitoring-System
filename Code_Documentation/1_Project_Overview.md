# *Project Title:* *Intelliguard : AI-Powered PPE Compliance Monitoring System*

## *Skills take away From This Project*
    - ●	Computer Vision with OpenCV & YOLO
    - ●	Object Detection & Fine-tuning Models
    - ●	Face Recognition for Secure Login
    - ●	Streamlit App Development
    - ●	AWS Integration (S3, RDS)
    - ●	NLP with LLMs & LangChain Agent
    - ●	SQL Query Handling via Chatbot
    - ●	Email Automation using SMTP
    - ●	Logging & Monitoring using TensorBoard
    - ●	Data Pipeline & Workflow Automation


## *Domain*
    - ●	Industrial Safety & Compliance
    - ●	Manufacturing
    - ●	AI in Workplace Monitoring
    - ●	Computer Vision & NLP Integration

## *Problem Statement:*
    - Build a computer vision–powered object detection system to monitor PPE (Personal Protective Equipment) compliance in manufacturing settings. 
    - The system should detect violations (like missing helmets or gloves) from video/image feeds and log anomalies to a cloud database. 
    - An intelligent dashboard with face-based login, anomaly monitoring, and chatbot querying is required for real-time decision-making.




## *Business Use Cases:*
    - ●	Real-time workplace safety monitoring in factories and warehouses
    - ●	Automated compliance checks to reduce manual inspections
    - ●	Health & safety audits with cloud-based violation logs
    - ●	Executive dashboards for department heads to analyze safety data
    - ●	Generative AI chatbot for querying workplace compliance status

## *Approach:*
*Model Training:* 
    - Use YOLO (e.g., YOLOv5/YOLOv8) for training on a PPE object detection dataset.

*Streamlit App:*
    - ●	Face/PIN-based login
    - ●	Upload image/video feed for detection
    - ●	Show detection output with bounding boxes
    - ●	Log violations to AWS RDS

*Database Design:*
    - ●	Table 1: Metadata + anomaly status
    - ●	Table 2: Violation-level details (e.g., no_mask, no_helmet)

*Automation:*
    - ●	Export violation logs as CSV
    - ●	Send auto-email alerts to safety heads

*Chatbot Agent:*
    - ●	Use LangChain with an SQL agent
    - ●	Natural language queries to RDS for anomaly insights

*Results:*
    - ●	A real-time PPE compliance monitoring system using a web UI
    - ●	Accurate object detection of both compliance and violation categories
    - ●	Logged and structured violation data in AWS RDS
    - ●	Face-authenticated secure access for uploading/testing
    - ●	AI-powered chatbot for seamless querying of PPE     - violation data
    - ●	Automated reporting to concerned teams

*Project Evaluation metrics:*
    - ●	Model Accuracy (mAP, precision, recall) for object detection
    - ●	Face Recognition Accuracy
    - ●	Database Logging Accuracy (no failed inserts)
    - ●	Response Time for chatbot queries
    - ●	Detection Latency for image/video uploads
    - ●	System Usability of Streamlit app

*Technical Tags:*
Computer Vision, YOLO, OpenCV, Streamlit, AWS S3, AWS RDS, Face Recognition, SMTP, LLM, LangChain, SQL Agent, TensorBoard, Anomaly Detection

*Data Set:*
*Format:* Images (JPEG/PNG) with YOLO annotations
*Classes :* ['glove', 'goggles', 'helmet', 'mask', 'no-suit', 'no_glove', 'no_goggles', 'no_helmet', 'no_mask', 'no_shoes', 'shoes', 'suit']


*Data Set Explanation:*
Images contain workers with/without required PPE gear in industrial settings
Annotations specify bounding boxes and class labels
Preprocessing may include:
●	Resizing images
●	Converting annotations to YOLO format
●	Splitting into train/val/test sets
●	Normalizing bounding box values

*Project Deliverables:*
●	YOLO-based custom object detection model
●	Fully functional Streamlit app:
○	Face login or PIN/password option
○	Image/video upload and detection output
○	RDS-based logging and CSV generation
○	Email alert automation
○	LLM chatbot for data querying
●	Source code with documentation
●	Database schema and scripts
●	Project Report / README

*Project Guidelines:*
●	Use version control (GitHub/GitLab) with regular commits
●	Follow clean coding standards and modular structure
●	Document all functions and components
●	Use .env or config files for sensitive keys (AWS, SMTP)
●	Log training metrics using TensorBoard
●	Keep requirements.txt updated
●	Validate detection and chatbot functionality using test cases
●	Write README with instructions on setup, usage, and deployment
