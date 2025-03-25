import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("✅ Бот успешно запущен! Напишите /ping для проверки.")

def ping(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("📍 Pong! Бот работает корректно.")

def main():
    updater = Updater(TELEGRAM_API_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ping", ping))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
