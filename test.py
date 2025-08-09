from dotenv import load_dotenv
import os

load_dotenv()

db_pass = os.getenv('DB_PASS')
db_user = os.getenv('DB_USER')

print(f"db_pass = {db_pass}")
print(f"db_user = {db_user}")
