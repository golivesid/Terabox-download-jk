from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Telegram Bot Token
MONGO_URI = os.getenv("MONGO_URI")  # MongoDB Connection String
TERABOX_API = os.getenv("TERABOX_API")  # Terabox API Key (Optional)
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))  # Admin Telegram ID (Default: 0)
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Forcing Subscription Channel ID
