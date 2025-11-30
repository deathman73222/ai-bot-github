#!/bin/bash
# Linux/macOS shell script to run AI Bot

cd "$(dirname "$0")"

# Check if venv exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing requirements..."
    pip install -r requirements.txt
fi

echo "Starting AI Bot..."
python run_ai_bot.py
