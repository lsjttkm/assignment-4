# this is the app/alpha.py file

import os
from dotenv import load_dotenv

load_dotenv() #looks in the .env file for environment variables

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")