# Telegram Bot

A modern Telegram bot built with Python using the `python-telegram-bot` library. This bot provides a foundation for building interactive Telegram applications with support for commands and message handling.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)

## ✨ Features

- **Command Handling**: Responds to `/start` command with a welcome message
- **Message Echo**: Echoes back text messages sent by users
- **Environment-based Configuration**: Uses `.env` file for secure token management
- **Async/Await Support**: Built with modern Python async/await patterns
- **Extensible Architecture**: Easy to add new commands and handlers


## 📦 Prerequisites

- Python 3.13 or higher
- A Telegram Bot Token (obtain from [@BotFather](https://t.me/BotFather))
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd telegrambot
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or using the project configuration:
   ```bash
   pip install -e .
   ```

## ⚙️ Configuration

1. **Create a `.env` file** in the project root:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```

2. **Get your Bot Token**:
   - Open Telegram and search for [@BotFather](https://t.me/BotFather)
   - Send `/newbot` command
   - Follow the instructions to create a bot
   - Copy the token provided
   - Paste it in your `.env` file

## 🎯 Usage

1. **Start the bot**:
   ```bash
   python src/main.py
   ```

   Or if installed as a package:
   ```bash
   python -m src.main
   ```

2. **Interact with the bot**:
   - Open Telegram and search for your bot
   - Send `/start` to receive a welcome message
   - Send any text message to see it echoed back

## 📁 Project Structure

```
telegrambot/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # Main application entry point
│   └── requirements.txt     # Source-level dependencies
├── .env                     # Environment variables (not in git)
├── .gitignore              # Git ignore rules
├── pyproject.toml          # Project configuration and metadata
├── requirements.txt        # Project dependencies
└── README.md               # This file
```