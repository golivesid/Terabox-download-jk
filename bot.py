from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from config import API_TOKEN, CHANNEL_ID, FORCE_SUB, ADMINS
from database import add_user, check_user
import requests
import os

# ✅ Function to check Force Subscription
def check_subscription(user_id, bot):
    try:
        user_status = bot.get_chat_member(FORCE_SUB, user_id).status
        return user_status in ["member", "administrator", "creator"]
    except:
        return False

# ✅ /start Command Handler
def start(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    add_user(user_id)

    if FORCE_SUB and not check_subscription(user_id, context.bot):
        keyboard = [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{FORCE_SUB}")]]
        update.message.reply_text("🔒 You must join our channel to use this bot!", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    update.message.reply_text("👋 Welcome to the Terabox Downloader Bot! Send me a Terabox link to download.")

# ✅ Handle Terabox Link
def handle_message(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    text = update.message.text

    if "terabox.com" in text:
        update.message.reply_text("🔄 Processing your Terabox link... Please wait!")

        # Simulated File URL (Replace this with actual extraction logic)
        file_url = f"https://fake-terabox-download.com/{user_id}"

        # 📥 Send File as Document
        update.message.reply_document(document=file_url, filename="TeraboxFile.mp4", caption="🎬 Here is your file!")
    else:
        update.message.reply_text("❌ Invalid Terabox Link! Please send a valid link.")

# ✅ Admin Command: /stats
def stats(update: Update, context: CallbackContext):
    if update.message.chat_id in ADMINS:
        user_count = check_user(update.message.chat_id)
        update.message.reply_text(f"📊 Total Users: {user_count}")

# ✅ Main Function
def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
