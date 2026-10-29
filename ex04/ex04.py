import warnings

import spacy

warnings.filterwarnings("ignore", message=".*no word vectors loaded.*")

nlp = spacy.load("en_core_web_sm")

sentence_1 = "I want to buy shoes"
sentence_2 = "I would love to purchase running shoes"
sentence_3 = "I am in my room"

doc1 = nlp(sentence_1)
doc2 = nlp(sentence_2)
doc3 = nlp(sentence_3)

pairs = [
    ("sentence_1", "sentence_2", doc1, doc2),
    ("sentence_1", "sentence_3", doc1, doc3),
    ("sentence_2", "sentence_3", doc2, doc3),
]

for first_name, second_name, first, second in pairs:
    print(f"{first_name} vs {second_name}: {first.similarity(second)}")
