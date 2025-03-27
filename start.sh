#!/bin/bash

# Проверка, не запущен ли бот уже
if pgrep -f "bot.py" > /dev/null
then
    echo "Бот уже запущен"
else
    python3 bot.py &
fi

gunicorn dummy:app --bind 0.0.0.0:$PORT
