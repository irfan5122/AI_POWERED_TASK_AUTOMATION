import spacy

nlp = spacy.load("en_core_web_sm")  # Use smaller model for speed
text1 = "open whatsapp"
text2 = "open chrome"

for text in [text1, text2]:
    doc = nlp(text)
    print(f"📌 Analyzing: {text}")
    for token in doc:
        print(f"Token: {token.text}, POS: {token.pos_}, Lemma: {token.lemma_}, Dep: {token.dep_}")
