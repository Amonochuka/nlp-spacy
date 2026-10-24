import spacy
import os

nlp = spacy.load("en_core_web_sm")

path = os.path.join(os.path.dirname(__file__), "data", "news_amazon.txt")
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

doc = nlp(text)
for sent in doc.sents:
    has_bezos_prop = False
    for token in sent:
        if token.text == "Bezos" and token.pos_ == "PROPN":
            has_bezos_prop = True
            break
    if has_bezos_prop:
        print(sent.text.strip())
