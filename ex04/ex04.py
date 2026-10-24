import spacy

nlp = spacy.load("en_core_web_sm")
sentence_1 = "I want to buy shoes"
sentence_2 = "I would love to purchase running shoes"
sentence_3 = "I am in my room"

doc1 = nlp(sentence_1)
doc2 = nlp(sentence_2)
doc3 = nlp(sentence_3)

print(doc1.similarity(doc2))
print(doc1.similarity(doc3))
print(doc2.similarity(doc3))
