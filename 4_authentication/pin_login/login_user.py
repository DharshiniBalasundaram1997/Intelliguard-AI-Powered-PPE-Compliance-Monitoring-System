import toml # type: ignore
import getpass
import hashlib
import os


path = "C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Final Project - 1/Project6_Code/Intelliguard_PPE_Detection/4_authentication/pin_login/credentials.toml"

CRED_FILE = path


def hash_pin(pin):
    secrets = hashlib.sha256(pin.encode()).hexdigest() #This line is used to securely hash a user's PIN or password using the SHA-256 hashing algorithm. 
    return secrets


def load_credentials():
    if not os.path.exists(CRED_FILE):
        return {}
    return toml.load(CRED_FILE)


# #if running the below code in login_user.py file, then commeent the streamlit
# def login_user(username,pin):
#     creds = load_credentials()
#     print(f"Existing users: {list(creds.keys())}")


#     username = input("Enter username: ")
#     print("Username: ", username)

#     if not username:
#         print("❌ Username cannot be empty.")
#         return False

#     pin = getpass.getpass("Enter your PIN/password: ")
#     print("Password:", pin)

#     if not pin:
#         print("❌ PIN cannot be empty.")
#         return False

#     if creds.get(username) == hash_pin(pin):
#         print(f"✅ Welcome, {username}")
#         return True
#     else:
#         print("❌ Invalid credentials.")
#         return False
    
#     return username,pin
    

#For streamlit purpose
def login_user(username, pin):
    creds = load_credentials()

    if not username or not pin:
        return False

    stored_hashed_pin = hash_pin(pin)
    stored_username = creds.get(username)

    return stored_hashed_pin == stored_username

    
if __name__ == "__main__":
    login_user()