import os

API_ID    = os.environ.get("API_ID", "30827233")
API_HASH  = os.environ.get("API_HASH", "07f8d7e1c1f2cc3576503dd0ea183881")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "9181409122:AAF8aNT_gbfuK4Neb97IMBhLhMs6uz54n_Y") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
