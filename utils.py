import os
import json
from datetime import datetime

SAVE_DIR = "data/conversations"
CONVO_STATE_PATH = "data/last_session.json"

def ensure_dirs():
    os.makedirs(SAVE_DIR, exist_ok=True)

def save_conversation(chat_history):
    ensure_dirs()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(SAVE_DIR, f"conversation_{timestamp}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(0, len(chat_history), 2):
            user = chat_history[i]["content"]
            assistant = chat_history[i + 1]["content"]
            f.write(f"Utilisateur : {user}\nAssistant : {assistant}\n\n")
    return filename

def save_chat_state(chat_history):
    ensure_dirs()
    with open(CONVO_STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(chat_history, f, ensure_ascii=False, indent=2)

def load_chat_state():
    if os.path.exists(CONVO_STATE_PATH):
        with open(CONVO_STATE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
