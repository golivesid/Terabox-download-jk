import os

API_TOKEN = os.getenv("API_TOKEN", "your_bot_token")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://username:password@cluster.mongodb.net/myDatabase?retryWrites=true&w=majority")
CHANNEL_ID = os.getenv("CHANNEL_ID", "@your_channel")
ADMINS = list(map(int, os.getenv("ADMINS", "123456789").split()))
FORCE_SUB = os.getenv("FORCE_SUB", "@your_channel")  # Force Subscription Channel
