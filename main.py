import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Ambil token dari environment variables (Railway)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ASI1_API_KEY = os.getenv("ASI1_API_KEY")
ASI1_API_URL = "https://api.asi1.ai/v1/chat/completions"

def chat_with_asi1(text):
    headers = {"Authorization": f"Bearer {ASI1_API_KEY}"}
    payload = {
        "model": "asi1-mini",
        "messages": [{"role": "user", "content": text}],
        "temperature": 0.7,
        "max_tokens": 100
    }
    response = requests.post(ASI1_API_URL, json=payload, headers=headers)
    return response.json()["choices"][0]["message"]["content"]

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Halo! Kirimkan pesan dan aku akan menjawab menggunakan ASI1: Mini!")

def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text
    bot_reply = chat_with_asi1(user_text)
    update.message.reply_text(bot_reply)

updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()
