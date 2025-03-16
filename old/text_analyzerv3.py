import spacy
import inspect
import lib_automata.automate as auto

KNOWN_APPS = {"chrome", "whatsapp", "filemanager", "brave", "weather", "store"}

def execute_commands(actions, objects, text):
    print("executing commands..")
    for action in actions:
        if action == "create":
            auto.create_file(text)
        elif action == "open":
            print("opening")
            print("Extracted objects:", objects)
            if objects:
                auto.open_app(objects[0])
            else:
                print("⚠ No object detected for 'open'")
        elif action == "delete":
            auto.delete_file()
        elif action == "search":
            if objects:
                auto.search_file(objects[0])
            else:
                print("⚠ No object detected for 'search'")

def process_command(data):
    nlp = spacy.load("en_core_web_trf")
    print("pocessing command ...")
    text = data
    doc = nlp(text)
    actions = []
    objects = []

    for token in doc:
        if token.pos_ == "VERB":
            actions.append(token.lemma_)  # Extract actions
        elif token.pos_ in ["NOUN", "PROPN"] or token.text.lower() in KNOWN_APPS:
            objects.append(token.text)

    execute_commands(actions, objects, text)

    print("command processed 😌")
    return actions, objects
