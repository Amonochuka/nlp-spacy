import spacy

nlp = spacy.load("en_core_web_sm")
text = "Tokenize this sentence. And this one too."
doc = nlp(text)
for token in doc:
    print(token.text)
