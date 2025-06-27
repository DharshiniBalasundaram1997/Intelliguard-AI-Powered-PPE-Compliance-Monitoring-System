import psycopg2
import os
from dotenv import load_dotenv

# Load credentials from the custom .env file in database_7 folder
base_path = os.getcwd()
cred_path = os.path.abspath(os.path.join(base_path, "database_7", "aws_rds_cred.env"))

print("-------RDS Credential Path-------")
print("Base Path:", base_path)
print("RDS Credential Path:", cred_path)

# Fetch the containing folder (i.e., 'database_7')
database_folder = os.path.dirname(cred_path)

print(f"In {database_folder} folder, Is aws_rds_cred file really exists?", os.path.isfile(cred_path)) 

if os.path.isfile(cred_path):
    load_dotenv(dotenv_path=cred_path)
    print("✅ Loaded AWS RDS credentials from .env file\n")
else:
    print("❌ .env file not found at:", cred_path, "\n")


# --- Function to connect to the default 'postgres' database ---
def connect_to_postgres():
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database="postgres",
            port=5432
        )
    except Exception as e:
        print("❌ Error connecting to 'postgres' DB:", e)
        return None

# --- Function to connect to the target 'violation_logs_db' database ---
def connect_to_violation_logs_db():
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME"),
            port=5432
        )
    except Exception as e:
        print("❌ Error connecting to 'violation_logs_db':", e)
        return None
