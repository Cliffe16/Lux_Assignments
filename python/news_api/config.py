import os
from dotenv import load_dotenv

# Call function to load environmnet variables
load_dotenv()

# Assign api key to a varibale
NEWS_API_KEY = os.getenv('API_KEY')
