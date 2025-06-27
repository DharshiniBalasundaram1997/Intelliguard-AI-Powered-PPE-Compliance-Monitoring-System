# *🚀 Project Workflow / Approach:*

## **📦 Model Training (YOLO):**
- Dataset: PPE Safety Dataset
- Classes: 12 classes incl. both PPE present and missing categories
- Format: YOLO annotations (.txt)
- Preprocessing:
   - Resize images
   - Normalize bounding boxes
   - Split into Train/Val/Test

## **🖥️ Streamlit App Features**
- Secure Login: Face recognition or PIN
- Image/Video Upload for Detection
- Real-time Violation Highlighting (Bounding Boxes)
- Detection Results Logging → AWS RDS

## **🗃️ Database Design (AWS RDS)**
- Table 1: File metadata + timestamp + login info + violation summary
- Table 2: Detailed violation records (e.g., "no_helmet" at x,y,w,h)

## **☁️ Cloud Integration**
- AWS S3: Store uploaded media
- AWS RDS: Log metadata and detailed violation records

## **🤖 Chatbot (LangChain + SQL Agent)**
- Natural language interface to RDS queries
- Example Queries:
    - “Show violations from last 3 days in Factory A”
    - “How many no_mask violations this month?”

## **📧 Automation**
- Auto-email alerts if violations exceed a threshold (e.g., >5/hour)
- CSV export for auditing/reporting
