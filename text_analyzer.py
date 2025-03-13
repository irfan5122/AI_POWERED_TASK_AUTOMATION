import spacy

nlp = spacy.load("en_core_web_trf")


def execute_comands(actions, objects, file_names, write_content):
    print(actions)
    print(objects)
    print(file_names)
    print(write_content)
    try:
        if actions[0] == "create":
            from lib_automata import creator
            creator.create_file("test_create.txt")

    except Exception:
        print(actions," - EMPTY")




def extract_write_content(doc, index):
    """Extracts content written after the 'write' command."""
    content = ""
    
    for i in range(index + 1, len(doc)):
        token = doc[i]
        
        # Capture quoted text
        if token.text.startswith(("'", '"')) and token.text.endswith(("'", '"')):
            content = token.text.strip("'\"")
            break
        
        # Capture unquoted words (e.g., "write hello")
        elif token.pos_ in ["NOUN", "PROPN", "X"] and token.text.lower() not in ["it", "this", "that"]:
            content = token.text
            break
    
    return content

def process_command(text):
    """Processes the command and extracts actions, objects, file names, and write content."""
    doc = nlp(text)

    actions = []
    objects = []
    file_names = []
    write_content = ""

    for i, token in enumerate(doc):
        if token.pos_ == "VERB":
            actions.append(token.lemma_)  # Store verb in base form

            # If verb is "write", call extract_write_content
            if token.lemma_ == "write":
                write_content = extract_write_content(doc, i)

        # Capture objects but exclude pronouns like "it"
        elif token.pos_ in ["NOUN", "PROPN"] and token.text.lower() not in ["it", "this", "that"]:
            objects.append(token.text)

    # Detect filenames in "save it as <filename>" pattern
    for i in range(len(doc) - 3):
        if doc[i].lemma_ == "save" and doc[i + 1].text.lower() == "it" and doc[i + 2].text.lower() == "as":
            file_names.append(doc[i + 3].text)

    # Ensure filenames are not classified as objects
    objects = [obj for obj in objects if obj not in file_names]


    execute_comands(actions, objects, file_names, write_content)




    return actions, objects, file_names, write_content

# Example usage
'''text = "create a file, write 'hello' to it then save it as greeting.txt and close it"
actions, objects, file_names, write_content = process_command(text)

print("Actions:", actions)
print("Objects:", objects)
print("File Names:", file_names)
print("Write Content:", write_content)
'''