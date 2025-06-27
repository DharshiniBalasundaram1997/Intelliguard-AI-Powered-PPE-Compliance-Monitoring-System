import cv2
import os
# import face_recognition
import matplotlib.pyplot as plt

#Run below line, if runnig this file alone
# image_dir = "C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Final Project - 1/Project6_Code/Intelliguard_PPE_Detection/4_authentication/face_Recognition/known_faces_images"
#Run below line, if runnig this file alone

def face_detected(image_dir):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    any_face_detected = False

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                image_path = os.path.join(root, file)
                img = cv2.imread(image_path)

                if img is None:
                    continue

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                # if len(faces) > 0:
                   
                
                if len(faces) == 0:
                    print(f"⚠️ No face detected in {file} \n")
                else:
                    any_face_detected = True  # ✅ Detected at least one
                    print(f"✅ Detected {len(faces)} face(s) in {root}:{file} \n")
                    print("Only the image is seen close it.")
                    for (x, y, w, h) in faces:
                        face = img[y:y+h, x:x+w]
                        plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
                        plt.axis('off')
                        plt.title(f"Detected Face in {file}")
                        plt.show()
    return any_face_detected

#Run below line, if runnig this file alone
# face_detected(image_dir)
#Run below line, if runnig this file alone
                    

