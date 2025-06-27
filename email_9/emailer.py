import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load credentials from the custom .env file in email_9 folder
base_path = os.getcwd()
cred_path = os.path.abspath(os.path.join(base_path, "email_9", "email_cred.env"))

print("-------Email Credential Path-------")
print("Base Path:", base_path)
print("Email Credential Path:", cred_path)

# Fetch the containing folder (i.e., 'email_9')
database_folder = os.path.dirname(cred_path)

print(f"In {database_folder} folder, Is email_cred file really exists?", os.path.isfile(cred_path)) 

if os.path.isfile(cred_path):
    load_dotenv(dotenv_path=cred_path)
    print("✅ Loaded Email credentials from .env file\n")
else:
    print("❌ .env file not found at:", cred_path, "\n")



# Load from .env or set manually
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
user_from_email = os.getenv("SMTP_USERNAME")
user_password = os.getenv("SMTP_PASSWORD")


def send_violation_email(subject, body, to_emails):
    print("SMTP Server:", smtp_server)
    print("SMTP Port:", smtp_port)
    print("From Email:", user_from_email)

    # Create message
    msg = MIMEMultipart()
    msg["From"] = user_from_email
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Send email
    try:
        server = smtplib.SMTP(smtp_server, int(smtp_port))
        server.ehlo()
        server.starttls()
        server.ehlo()  # Re-identify after TLS
        server.login(user_from_email, user_password)
        server.sendmail(user_from_email, to_emails, msg.as_string())
        server.quit()
        print("Email sent Successfully")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    send_violation_email()