import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

def remember(key, value):
    memory = load_memory()
    memory[key.lower()] = value
    save_memory(memory)

def recall(key):
    memory = load_memory()
    return memory.get(key.lower(), "I don't remember that.")
