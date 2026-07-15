import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memories):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memories, file, indent=4)


def add_memory(user_id, user_message, assistant_reply):
    memories = load_memory()

    if user_id not in memories:
        memories[user_id] = []

    memories[user_id].append({
        "user": user_message,
        "assistant": assistant_reply
    })

    save_memory(memories)


def search_memory(user_id):
    memories = load_memory()

    if user_id not in memories:
        return ""

    history = ""

    for chat in memories[user_id][-5:]:
        history += f"""
User: {chat['user']}
Assistant: {chat['assistant']}

"""

    return history