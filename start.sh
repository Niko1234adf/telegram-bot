#!/bin/bash

# Сначала запускаем Flask dummy-сервер
gunicorn dummy:app --bind 0.0.0.0:$PORT &

# Затем запускаем Telegram-бота в основном процессе (без &)
python3 bot.py
