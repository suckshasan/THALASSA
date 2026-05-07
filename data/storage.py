import json
import os

from config import DATA_FILE

characters = {}
active_prompts = {}


def load_data():
    global characters

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f)

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        characters = json.load(f)



def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(characters, f, indent=4)