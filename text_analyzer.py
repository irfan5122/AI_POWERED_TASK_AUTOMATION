import torch
from transformers import pipeline
import lib_automata.automate as auto

# Initialize as None to indicate not loaded yet
nlp = None
ACTION_KEYWORDS = ["create", "open", "delete", "close", "launch", "remove",
                     "start", "exit", "make", "erase", "search","shutdown"]

def load_model():
    """Load the NLP model and return it"""
    global nlp
    if nlp is None:
        nlp = pipeline("fill-mask", model="distilroberta-base")
    return nlp

def execute_commands(actions, objects, text):
    print("executing commands..")

    try:
        for action in actions:
            if action == "create" or action == "make":
                auto.create_file(text)
            elif action == "open":
                print("opening")
                print("Extracted objects:", objects)
                if objects:
                    auto.open_app(objects[0])
                else:
                    print("⚠ No object detected for 'open'")
            elif action == "delete":
                auto.delete_file(text)
            elif action == "search":
                if objects:
                    auto.search(objects[0], text)
                else:
                    print("⚠ No object detected for 'search'")

            elif action == "close":
                auto.close_app(objects[0])

            elif action == "shutdown":
                auto.shutdown_system()
    except Exception:
        print("Command Error")

        

def load_app_names(filename="objects.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            app_names = [line.strip().lower() for line in file if line.strip()]  
        return app_names
    except FileNotFoundError:
        print("❌ Error: File not found!")
        return []

def process_command(text):
    # Ensure model is loaded
    load_model()
    
    actions = []
    objects = []
    words = text.split()

    for idx, word in enumerate(words):
        if word.lower() in ACTION_KEYWORDS:
            actions.append(word.lower())  
            if idx + 1 < len(words):  
                next_word = words[idx + 1].lower()
                if next_word in KNOWN_OBJECTS:
                    objects.append(next_word)  
    
    execute_commands(actions, objects, text)
    print("\n✅ Extracted Actions:", actions)
    print("✅ Extracted Objects:", objects)
    return actions, objects

KNOWN_OBJECTS = load_app_names()