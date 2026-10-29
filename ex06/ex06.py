import os
import re

import spacy

nlp = spacy.load("en_core_web_sm")

path = os.path.join(os.path.dirname(__file__), "data", "news_amazon.txt")
with open(path, "r", encoding="utf-8") as file:
    text = file.read()

paragraphs = re.split(r"\n\s*\n", text.strip())

index = 0
for paragraph in paragraphs:
    doc = nlp(paragraph)
    for sentence in doc.sents:
        index += 1
        mentions_bezos = any(
            token.text == "Bezos" and token.pos_ == "PROPN" for token in sentence
        )
        if mentions_bezos:
            print(f"{index}. {sentence.text.strip()}")
