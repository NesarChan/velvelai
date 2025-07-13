import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PORNPEN_API_KEY = os.getenv("PORNPEN_API_KEY")
