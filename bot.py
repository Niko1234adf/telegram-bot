import os
os.system("pip install python-telegram-bot==13.15")

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Получаем API-ключ из переменных окружения
TELEGRAM_API_TOKEN = os.getenv(7851181908:AAENbvghKJOJK0vrsseuKLyCUiyuTXrbIAA)

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
