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
            auto.delete_file(text)


        elif action == "search":
            if objects:
                auto.search(objects[0])
            else:
                print("⚠ No object detected for 'search'")




def process_command(data):
    nlp = spacy.load("en_core_web_sm") 
    doc = nlp(data)
    actions = []
    objects = []
    filename = None

   
    ACTION_WORDS = {"open", "search", "delete", "create"}

    for token in doc:
        print(f"Token: {token.text}, POS: {token.pos_}, Dep: {token.dep_}")  

       
        if token.text.lower() in ACTION_WORDS or token.pos_ == "VERB":
            actions.append(token.lemma_.lower())

      
        elif "." in token.text:
            filename = token.text

      
        elif token.dep_ in ["dobj", "pobj", "attr", "nmod"] or token.pos_ in ["NOUN", "PROPN"]:
            objects.append(token.text.lower())

    if filename:
        objects.append(filename)  

    print(f"📌 Extracted Actions: {actions}")
    print(f"📌 Extracted Objects: {objects}")
    execute_commands(actions, objects, data)
    return actions, objects
