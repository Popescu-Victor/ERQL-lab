from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("APP_USERNAME")
password = os.getenv("APP_PASSWORD")

print(f"Username: {username}")
print(f"Password: {password}")