# Thalassa Discord Bot

A Discord bot for managing characters and interactive prompts in the Thalassa universe.

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Bot Token
Set your Discord bot token as an environment variable:
```bash
export DISCORD_BOT_TOKEN="your_token_here"
```

### 3. Run the Bot
```bash
python bot.py
```

## Commands

### Admin Commands
- `!addcharacter <member> <name> <faction> <district> <reputation>` - Add a character to a player
- `!removecharacter <member>` - Remove a player's character
- `!listcharacters` - List all registered characters
- `!prompt <member> <text>` - Send a decision prompt to a player

### Player Commands
- `!me` - View your character information
- `!encourage` - Encourage the current prompt action
- `!discourage` - Discourage the current prompt action

## Project Structure
```
THALASSA/
├── bot.py                 # Main bot entry point
├── config.py              # Configuration
├── requirements.txt       # Dependencies
├── characters.json        # Character storage
├── models/
│   └── character.py       # Character data model
├── data/
│   └── storage.py         # Data persistence
└── commands/
    ├── admin.py           # Admin commands
    ├── player.py          # Player commands
    └── prompts.py         # Prompt system
```
