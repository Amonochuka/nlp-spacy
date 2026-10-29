import spacy

nlp = spacy.load("en_core_web_sm")
token = nlp("car")[0]

print(token.vector.shape)

total = float(token.vector[:20].sum())
print(float.as_integer_ratio(total))
