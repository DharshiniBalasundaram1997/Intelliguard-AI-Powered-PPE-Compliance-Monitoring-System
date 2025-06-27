import os
import sys


def setup_auth_paths():
    print("--------Set Up Auth Paths----------")
    base_path = os.getcwd()
    print("Base Path:", base_path, "\n")


    # Face recognition path
    face_recognition = os.path.abspath(os.path.join(base_path, "4_authentication", "face_Recognition"))
    print("-------Face Recognition Path-------:")   
    print("Base Path:", base_path)
    print("Face Recognition Path:", face_recognition) 
    print("Is Face Recognition folder really exists?:", os.path.isdir(face_recognition)) 
    if os.path.isdir(face_recognition):
        sys.path.append(face_recognition)
        print("✅ Face recognition path added to sys.path\n")
    else:
        print("❌ Face recognition path not recognized (directory missing)\n")


    # PIN login path
    pin_login_path = os.path.abspath(os.path.join(base_path, "4_authentication", "pin_login"))
    print("-------PIN Login Path-------:") 
    print("Base Path:", base_path)  
    print("PIN Login Path:", pin_login_path)
    print("Is PIN Login folder really exists?:", os.path.isdir(pin_login_path))
    if os.path.isdir(pin_login_path):
        sys.path.append(pin_login_path)
        print("✅ PIN login path added to sys.path\n")
    else:
        print("❌ PIN login path not recognized (directory missing)\n")

    #AWS S3 Bucket Path:
    aws_s3_integration = os.path.abspath(os.path.join(base_path, ".", "AWS_Integration_6"))
    print("-------AWS S3 Path-------:")   
    print("Base Path:", base_path) #or print(os.path.dirname(aws_s3_integration)) -> parent folder
    print("AWS S3 Bucket Path:",aws_s3_integration)
    print("Is AWS S3 folder really exists?:", os.path.isdir(aws_s3_integration)) 
    
    if os.path.isdir(aws_s3_integration):
        sys.path.append(aws_s3_integration)
        print(aws_s3_integration,"✅ Loaded AWS File Directory to sys.path\n")
    else:
        print("❌ AWS File Directory path not recognized (directory missing)\n")

    # AWS RDS Path
    aws_rds_path = os.path.abspath(os.path.join(base_path,".", "database_7"))
    print("-------RDS Credential Path-------:")   
    print("Base Path:", base_path)
    print("RDS Credential Path:", aws_rds_path)
    print("Is RDS Credential folder really exists?:", os.path.isdir(aws_rds_path)) 

    if os.path.dirname(aws_rds_path):
        sys.path.append(aws_rds_path)
        print("✅ Loaded AWS RDS credentials from folder\n")
    else:
        print("❌ folder not found at:", aws_rds_path, "\n")

    #Open_AI Cred 
    chatbot = os.path.abspath(os.path.join(base_path,".", "chatbot_8"))
    print("-------Chatbot Path-------:")   
    print("Base Path:", base_path)
    print("Chatbot Path:", chatbot)
    print("Is Chatbot folder really exists?:", os.path.isdir(chatbot))

    if os.path.dirname(chatbot):
        sys.path.append(chatbot)
        print("✅ Loaded Chatbot folder\n")
    else:
        print("❌ Folder not found at:", chatbot, "\n")

    #email Cred 
    email = os.path.abspath(os.path.join(base_path,".", "email_9"))
    print("-------email Path-------:")   
    print("Base Path:", base_path)
    print("email Path:", email)
    print("Is email folder really exists?:", os.path.isdir(email))

    if os.path.dirname(email):
        sys.path.append(email)
        print("✅ Loaded email folder\n")
    else:
        print("❌ Folder not found at:", email, "\n")

    return face_recognition, pin_login_path, aws_s3_integration, aws_rds_path, email


setup_auth_paths()

