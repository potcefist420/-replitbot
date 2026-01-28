# Telegram Piar Bot

## Overview
A Telegram bot built with Python and aiogram framework for promoting channels, groups, and bots in Telegram. Users can earn coins by completing tasks like subscribing to channels, viewing posts, and joining groups.

## Project Structure
```
├── main.py              # Entry point - starts the bot
├── loader.py            # Bot and dispatcher initialization
├── settings.ini         # Configuration file (bot token, settings)
├── data/
│   ├── config.py        # Config parser for settings.ini
│   ├── data.dat         # Pickle data file
│   └── data.db          # SQLite database
├── handlers/            # Message and callback handlers
│   ├── admin.py         # Admin commands
│   ├── chat.py          # Chat-related handlers
│   ├── earn.py          # Earning tasks handlers
│   ├── games.py         # Game handlers (dice, slots)
│   ├── profile.py       # User profile handlers
│   ├── promo.py         # Promotion handlers
│   └── referals.py      # Referral system handlers
├── filters/             # Custom message filters
├── keyboards/           # Inline and reply keyboards
├── middlewares/         # Middleware (throttling)
├── states/              # FSM states
└── utils/               # Utility functions
    ├── sqlite.py        # Database operations
    ├── messages.py      # Message templates
    └── qiwi.py          # QIWI payment integration
```

## Technology Stack
- **Language**: Python 3.11
- **Framework**: aiogram 2.x (Telegram Bot API wrapper)
- **Database**: SQLite (via aiosqlite)
- **HTTP Client**: aiohttp

## Configuration
Settings are stored in `settings.ini` and include:
- Bot token and admin IDs
- Channel/group settings
- Payment and pricing configuration
- Game settings
- Referral system settings

## Running the Bot
The bot runs via the "Telegram Bot" workflow which executes `python main.py`.

## Recent Changes
- **2026-01-27**: Initial import and setup in Replit environment
