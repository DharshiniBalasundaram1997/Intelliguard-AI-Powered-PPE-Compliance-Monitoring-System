import pandas as pd

def create_env_from_csv(env_path="AWS_Integration_6/cred.env"):
    # Path to your Excel file
    csv_path = "AWS_Integration_6/rootkey.csv"
    print("-------AWS Access Key Path: -------")
    print(csv_path)

    # Read the Excel file
    df = pd.read_csv(csv_path)
    # print("csv file contents: ")
    # print(df)

    # Get the first row's credentials
    access_key = df.iloc[0]["Access key ID"]
    # print(access_key)

    secret_key = df.iloc[0]["Secret access key"]
    # print(secret_key)


    # Output .env path
    env_path = "AWS_Integration_6\cred.env"  # Or ".env" if you want it at root
    print("Saving AWS Credentails Path:",env_path)

    with open(env_path, "w") as f:
        f.write(f"AWS_ACCESS_KEY_ID={access_key}\n")
        f.write(f"AWS_SECRET_ACCESS_KEY={secret_key}\n")
        f.write(f"AWS_REGION=ap-south-1\n") #  my region - Asia Pacific (Mumbai) ap-south-1
        f.write(f"S3_BUCKET=intelliguard-ppe-uploads\n")

    print(f"✅ .env file written to {env_path}\n")
