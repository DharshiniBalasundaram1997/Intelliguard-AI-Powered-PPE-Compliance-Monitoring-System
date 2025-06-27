from ultralytics import YOLO
import os
import shutil
import yaml
from collections import Counter
import json


# Load the model once globally
model_path = "C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Final Project - 1/Project6_Code/Intelliguard_PPE_Detection/ppe_training/ppe_compliance_model/weights/best.pt"
model = YOLO(model_path)


yaml_path = "C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Final Project - 1/Project6_Code/Intelliguard_PPE_Detection/PPE_Images_dataset/data.yaml"

# Load class names from data.yaml
def load_class_names(yaml_path):
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    return data['names']



# Required PPE items for compliance
REQUIRED_PPE = set(load_class_names(yaml_path))

#POstive Items presnt in yaml
positive_items_present_in_yaml = set()
for i in REQUIRED_PPE:
    if not (i.startswith("no_") or i.startswith("no-")):
        positive_items_present_in_yaml.add(i)
print("List of Compliance_Items present in yaml file:", positive_items_present_in_yaml, "\n")

#NEgative Items presnt in yaml
# Step 1: Get only "no_" or "no-" variants from REQUIRED_PPE
violation_items_present_in_yaml = set()
for i in REQUIRED_PPE:
    if i.startswith("no_") or i.startswith("no-"):
        violation_items_present_in_yaml.add(i)
print("List of Violation_Items present in yaml file:", violation_items_present_in_yaml, "\n")





####Enable the below lines if executing this file alone###
#For All Images: use the below path
# image_path = "C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Final Project - 1/Project6_Code/Intelliguard_PPE_Detection/PPE_Images_dataset/test/images"

#For Single image use below path
# image_path = "C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Final Project - 1/Project6_Code/Intelliguard_PPE_Detection/PPE_Images_dataset/test/images/packing958_jpg.rf.2d9e1e0fed8d49d75115713c279f3a84.jpg"
####Enable the below lines if executing this file alone###



def detect_objects(image_path):
    # Run detection on imgage - predict
    results = model.predict(image_path, save=True, conf=0.1)
    print("Predicted Results:",results,"\n") # Shows bounding boxes, confidence, class

    # Save YOLO output image from the auto-generated directory to run/detect
    yolo_output_dir = results[0].save_dir  # e.g., by default it will save in c:\\Users\\dhars\\runs\\detect\\predict'
    print("Default path where image will be saved: ",yolo_output_dir)
    
    
    base_name = os.path.basename(yolo_output_dir)
    print("Base Name: ",base_name)

    # Your destination base path
    destination_dir = os.path.join("runs", "detect", base_name)
    print("Moving the results from Default path to runs\detect folder:", destination_dir)

    # Ensure uniqueness # If folder exists, add suffix like _1, _2, etc.
    counter = 0
    while os.path.exists(destination_dir):
        destination_dir = os.path.join("runs", "detect", f"{base_name}_{counter}")
        counter += 1

    # Move the folder results
    shutil.copytree(yolo_output_dir, destination_dir)

    print(f"✅ Results moved to: {destination_dir}\n")

    # Get path to saved prediction image
    result_image_path = None
    for fname in os.listdir(destination_dir): #['005298_jpg.rf.f88eed797ecd501d2d63e6961e2bbb76.jpg',..]
        if fname.endswith((".jpg", ".png")):
            result_image_path = os.path.join(destination_dir, fname) ## will get o/p like ->  C:\Users\dhars\Downloads\Dhass\codeing\GUVI\2. MainBoot\4.Project_Code\Final Project - 1\Project6_Code\Intelliguard_PPE_Detection\runs\detect\predict\'005298_jpg.rf.f88eed797ecd501d2d63e6961e2bbb76.jpg'
            break

    # --- Optional: PPE Violation Check ---
    boxes = results[0].boxes #will get attributes of boxes
    print("----Attributes of boxes----")
    print(boxes,"\n")

    # print(boxes.conf) #tensor
    # print(type(boxes.conf), "\n") #type 

    

    violations_conf_score = []
    positives_conf_score = []

    detected_items = set()
    unique_detected_items = []

    no_of_violation_class = []
    no_of_Positive_class = []

    for cls_id, conf_score in zip(boxes.cls.tolist(), boxes.conf.tolist()):
      print("------Class + Conf Score Detected from each frame in the Image--------")
      print("Class ID:", cls_id)

      class_name = results[0].names[int(cls_id)]  # convert ID to name
      print(f"Class Name: {class_name} | Confidence Score: {conf_score:.2f}") #Unique Items Detected from each frame in the Image , aling with name and score

      if class_name.startswith("no_") or class_name.startswith("no-"):
        # no_of_violation_class_name = results[0].names[int(cls_id)]  # convert ID to name
        no_of_violation_class.append(class_name)
        print(f"Violation Class Name: {no_of_violation_class}")
        
        violations_conf_score.append(conf_score)
        print("Violation Confidence Score:", violations_conf_score, "\n")

      else: 
        # no_of_Positive_class = results[0].names[int(cls_id)]  # convert ID to name
        no_of_Positive_class.append(class_name)
        print(f"Positive Class Name: {no_of_Positive_class}")

        positives_conf_score.append(conf_score)
        print("Positive Confidence Score:", positives_conf_score, "\n")

      detected_items.add(class_name.lower())  # add to set
      unique_detected_items = list(detected_items)

    
    print("--------Total Items & Conf Score Detected from Image--------")
    # print("Total Items Detected from Image:", detected_items)
    print("Unique Items Detected from Image:",unique_detected_items)

    print("Total No.Of.Violation Class Names:", no_of_violation_class)
    print("Total Violation Confidence Scores:",violations_conf_score)

    print("Total No.Of.Positive Class Names: ",no_of_Positive_class)
    print("Total Positive Confidence Scores:",positives_conf_score,"\n")
    
    

    # Separate detections into normal/positives and violations
    print("--------Separate detections into normal/positives and violations--------")
    violations = set()
    for item in unique_detected_items: #for item in detected_items
        if item.startswith("no_") or item.startswith("no-"):
            violations.add(item)
    print("Violation Items: ",violations)

    positives = set()
    for item in unique_detected_items: #for item in detected_items
       if item not in violations:
           positives.add(item)
    print("Positive Items: ",positives)

    # Filter required PPE items that are neither detected nor violated
    print("\n","--------Filter required PPE items that are neither detected nor violated--------")
    missing_items = set()

    for item in violation_items_present_in_yaml:
        print("Items: ",item)
        
        # Handle both "no_" and "no-" cases
        actual_ppe = item.replace("no_", "").replace("no-", "") #no-glove -> glove
        print("actual_ppe:", actual_ppe,"\n")

        no_variant_1 = f"no_{actual_ppe}"
        print("no_variant_1:", no_variant_1)

        no_variant_2 = f"no-{actual_ppe}"
        print("no_variant_2:", no_variant_2, "\n")
        
        if actual_ppe not in positives and no_variant_1 not in violations and no_variant_2 not in violations:
            missing_items.add(item)
    print("Missing PPE items that are neither detected nor violated:",missing_items, "\n")
    
    print("---Summary---")
    print("Violations Detected:", violations)
    print("Missing Items:", missing_items)
    print("PPE Detected (Compliant):", positives, "\n")

    
    # Combine for total report
    all_violations_detected = violations|missing_items #union() combines all unique items and No duplicates        all_violations = violations.union(missing_items)
    
    if all_violations_detected:
        print(f"🚨 All Violations Detected in the image!: {', '.join(all_violations_detected)}")

        ## Count how many times each violation was detected
        violation_counts = Counter([cls.lower() for cls in no_of_violation_class if cls.startswith("no_") or cls.startswith("no-")])
        for item in sorted(violation_items_present_in_yaml):  # sorted for consistent order
           print(f"{item} - {violation_counts.get(item, 0)}")
    else:
        print("✅ All required PPE detected  in the image.")
    if positives:
        print(f"🟢 Compliant PPE Detected  in the image: {', '.join(positives)}")

        ## Count how many times each positives was detected
        positive_counts = Counter([cls.lower() for cls in no_of_Positive_class if cls not in violation_counts])
        for item in sorted(positive_items_present_in_yaml):
           print(f"{item} - {positive_counts.get(item, 0)}")
    else:
        print("⚠️ No compliant PPE detected.")
    
    # print(all_violations_detected)
    return result_image_path, violations, missing_items, positives, violations_conf_score, unique_detected_items,no_of_violation_class


####Enable the below lines if executing this file alone###
# detect_objects(image_path)
####Enable the below lines if executing this file alone###
