from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Telegram Bot Token
MONGO_URI = os.getenv("mongodb+srv://sampledhdj6:Y308LujZfMesIkpQ@cluster0.j9ha2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # MongoDB Connection String
TERABOX_API = os.getenv("TERABOX_API")  # Terabox API Key (Optional)
ADMIN_ID = int(os.getenv("6644473960", ))  # Admin Telegram ID (Default: 0)
CHANNEL_ID = os.getenv("2255827235")  # Forcing Subscription Channel ID
