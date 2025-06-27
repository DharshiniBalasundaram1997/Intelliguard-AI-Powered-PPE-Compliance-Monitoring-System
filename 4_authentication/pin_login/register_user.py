import toml # type: ignore
import getpass
import hashlib
import os

path = "C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Final Project - 1/Project6_Code/Intelliguard_PPE_Detection/4_authentication/pin_login/credentials.toml"
CRED_FILE = path

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

def load_credentials():
    if not os.path.exists(CRED_FILE):
        return {}
    return toml.load(CRED_FILE)

def save_credentials(data):
    with open(CRED_FILE, "w") as f:
        toml.dump(data, f)




# #if running the below code in register_user.py file, then commeent the streamlit
# def register_user(username,pin):
#     creds = load_credentials()

#     ## ✅ Proactively remove any empty keys
#     if "" in creds:
#         print("⚠️ Found and removed empty username from credentials.")
#         del creds[""]
#         save_credentials(creds)

#     print(f"📋 Existing User Lists: {list(creds.keys())}")
    
#     print("📥 To Enter New Registration")

#     username = input("Enter new username: ").strip()
#     print(f"Entered Username: '{username}'")

#     if not username:
#         print("❌ Username cannot be empty.")
#         return False

#     if username in creds:
#         print("⚠️ Username already exists.")
#         return False

#     pin = getpass.getpass("Set your PIN/password: ").strip()
#     confirm = getpass.getpass("Confirm your PIN/password: ").strip()

#     if not pin:
#         print("❌ PIN cannot be empty.")
#         return False
    
#     if pin != confirm:
#         print("❌ PINs do not match.")
#         return

#     creds[username] = hash_pin(pin)
#     save_credentials(creds)

#     print(f"✅ User '{username}' registered successfully.")
#     print(f"📋 New Users  Lists: {list(creds.keys())}")
#     return True

# if __name__ == "__main__":
#     register_user()



#For streamlit purpose
def register_user(username, pin):
    creds = load_credentials()

    if not username:
        return False, "❌ Username cannot be empty."

    if username in creds:
        return False, "⚠️ Username already exists."

    if not pin:
        return False, "❌ PIN cannot be empty."

    creds[username] = hash_pin(pin)
    save_credentials(creds)

    return True, f"✅ User '{username}' registered successfully."


if __name__ == "__main__":
    print("🔧 This script is designed to be used via Streamlit. Run it through the UI.")
    










#This line is used to securely hash a user's PIN or password using the SHA-256 hashing algorithm. 
# hashlib.sha256(pin.encode()).hexdigest() 

# -> pin.encode()
     # Converts the pin (a string) into bytes.
     # Hash functions work on bytes, not strings, so encoding is necessary.
     # Example:
        # "1234".encode()  # → b'1234'
        #"ini".encode() # Output: b'Ini123'



# -> hashlib.sha256(...)
     # Applies the SHA-256 hashing algorithm to the byte-encoded PIN.
     # SHA-256 is part of the SHA-2 family and is widely used for secure hashing.
     # It produces a fixed-length 64-character hexadecimal hash.

# -> .hexdigest()
     # Converts the raw hash bytes into a readable hexadecimal string.
     # This is what you store in your credentials.toml file