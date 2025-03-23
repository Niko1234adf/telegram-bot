#!/bin/bash

# Запуск бота в фоне
python3 bot.py &

# Запуск dummy-сервера (Flask) через Gunicorn
gunicorn dummy:app --bind 0.0.0.0:$PORT
