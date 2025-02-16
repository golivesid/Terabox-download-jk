from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import requests
import pymongo
import os

# Configurations
from config import BOT_TOKEN, MONGO_URI, CHANNEL_ID

# MongoDB Setup
client = pymongo.MongoClient(MONGO_URI)
db = client["terabox_bot"]
users_col = db["users"]

# Function to check subscription
def check_subscription(user_id, context):
    try:
        chat_member = context.bot.get_chat_member(CHANNEL_ID, user_id)
        return chat_member.status in ["member", "administrator", "creator"]
    except:
        return False

# Start Command
def start(update: Update, context: CallbackContext):
    user_id = update.message.chat_id

    if not check_subscription(user_id, context):
        keyboard = [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL_ID}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Please join our channel to use this bot.", reply_markup=reply_markup)
        return
    
    # User Registration
    if not users_col.find_one({"user_id": user_id}):
        users_col.insert_one({"user_id": user_id})

    update.message.reply_text("Send me a Terabox link to download.")

# Handle Messages
def handle_message(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    text = update.message.text

    if "terabox" in text:
        update.message.reply_text("Processing your Terabox link...")

        # Fake download process (actual logic to be added)
        file_url = "https://example.com/downloaded_file.mp4"  # Placeholder

        context.bot.send_document(chat_id=user_id, document=file_url, caption="Here is your file.")
    else:
        update.message.reply_text("Please send a valid Terabox link.")

# Main Function
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
