import os
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# ✅ API-ключ бота (НЕ используем os.getenv, а передаем напрямую)
TELEGRAM_API_TOKEN = "7851181908:AAENbvghKJOJK0vrsseuKLyCUiyuTXrbIAA"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("✅ Бот успешно запущен! Напишите /ping для проверки.")

def ping(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("📍 Pong! Бот работает корректно.")

def main():
    # ✅ Создаем Updater и Dispatcher
    updater = Updater(token=TELEGRAM_API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # ✅ Добавляем обработчики команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ping", ping))

    # ✅ Даем паузу перед запуском
    time.sleep(5)

    # ✅ Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
