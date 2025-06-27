import boto3
import os
from dotenv import load_dotenv

# This imports the load_dotenv function from the python-dotenv package.
# python-dotenv is a Python package that allows you to load environment variables from a .env file into your Python script.

# The .env file is not a Python module or package. Adding its path to sys.path does nothing for your environment variables.
# We will get below values as None
# access_key = os.getenv("AWS_ACCESS_KEY_ID")
# secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
# region = os.getenv("AWS_REGION")
# bucket_name = os.getenv("S3_BUCKET")

# So Use load_dotenv:
# load_dotenv(dotenv_path=aws_integration)
# This line tells Python to read your .env file and load the variables inside into the environment (os.environ). 
# Without it, your os.getenv("AWS_ACCESS_KEY_ID") and others will return None.

# Step 1: Import the function from sibling file
from write_env_from_excel import create_env_from_csv

# Step 2: Call it to ensure .env is written
create_env_from_csv()


print("-------AWS S3 Bucket Integration Path-------")
base_path = os.getcwd()
print("Base Path:", base_path)
aws_integration = os.path.abspath(os.path.join(base_path, "AWS_Integration_6","cred.env"))
print("AWS S3 Bucket Integration Path", aws_integration)

# Fetch the containing folder (i.e., 'AWS_Integration_6')
database_folder = os.path.dirname(aws_integration)
print(f"In {database_folder}, Is -cred.env file really exists?", os.path.isfile(aws_integration)) 

if os.path.isfile(aws_integration):
    load_dotenv(dotenv_path=aws_integration)
    print("✅ Loaded credentials from .env file\n")
else:
    print("❌ cred.env file not found\n")

access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION")
bucket_name = os.getenv("S3_BUCKET")

# # Create S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
)

def upload_file_to_s3(file_path, file_name):
    """
    Uploads a file to AWS S3 and returns its public URL
    """
    try:
        s3.upload_file(file_path, bucket_name, file_name)

        # s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=file_name) # EITHER ENABLE THE ACL IN MY BUCKET -> ACL OR ENTER THE CODE IN BUCKET POLICY

        s3_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{file_name}" #This URL can be fetched from bucket -> objects
        print("file sent to aws")

        
        return s3_url
    except Exception as e:
        print("Error uploading to S3:", e)
        return None

# file_path = "C:/Users/dhars/Downloads/Dhass/codeing/GUVI/2. MainBoot/4.Project_Code/Final Project - 1/PPE_Images_dataset/test/images/packing91_jpg.rf.0381671ca4edb9d3dbc5244893d4b2f9.jpg"
# file_name = "vio_pic"
# upload_file_to_s3(file_path, file_name)

