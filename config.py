from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
SPREAD_THRESHOLD = float(os.getenv("SPREAD_THRESHOLD", 50))
LAST_ALERT_TIME = float(os.getenv("LAST_ALERT_TIME", 0))
ALERT_COOLDOWN = float(os.getenv("ALERT_COOLDOWN", 60))