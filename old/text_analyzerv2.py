import spacy
import inspect
import lib_automata.automate as auto
def execute_commands(actions, objects,text):
    for action in actions:
        if action == "create":
            auto.create_file(text)
        elif action == "open":
            print(objects)
            auto.open_app(objects[0])
        elif action == "delete":
            auto.delete_file()
        elif action == "search":
            auto.search()
    

def process_command(data):
    nlp = spacy.load("en_core_web_trf")
    text = data
    doc = nlp(text)
    actions = []
    objects = []
    
    # Process tokens
    for token in doc:
        if token.pos_ == "VERB":
            actions.append(token.lemma_)  # Lemmatizing verbs for consistency
        elif token.pos_ in ["NOUN", "PROPN"]:
            objects.append(token.text)
        
    # Handling prepositions and compound nouns
    compound_objects = []
    skip_next = False
    for i, token in enumerate(doc):
        if skip_next:
            skip_next = False
            continue
        if token.dep_ == "compound" and i + 1 < len(doc):
            compound = f"{token.text} {doc[i + 1].text}"
            compound_objects.append(compound)
            skip_next = True
        elif token.dep_ in ["dobj", "pobj", "attr"]:
            compound_objects.append(token.text)
    # Deduplicate and merge lists
    objects = list(set(objects + compound_objects))

    execute_commands(actions, objects,text)
    '''print("Actions:", actions)
                print("Objects:", objects)
            '''
    return actions, objects