import os
import json
from OreskossTCG.models import Deck

DATA_DIR = "data"

def save_decks(decks):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(os.path.join(DATA_DIR, "decks.json"), "w") as f:
        json.dump([deck.to_dict() for deck in decks], f, indent=4)

def load_decks():
    try:
        with open(os.path.join(DATA_DIR, "decks.json"), "r") as f:
            deck_data = json.load(f)
            return [Deck.from_dict(d) for d in deck_data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
