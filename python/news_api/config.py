import os
from dotenv import load_dotenv

# Call function to load environmnet variables
load_dotenv()

# Assign api key to a varibale
NEWS_API_KEY = os.getenv('API_KEY')
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB = os.getenv("DB")
