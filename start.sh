#!/bin/bash

# Запуск бота в фоне
python3 bot.py &

# Запуск dummy.py — нужен для Render, чтобы "думал", что есть веб-сервер
gunicorn dummy:app --bind 0.0.0.0:$PORT
