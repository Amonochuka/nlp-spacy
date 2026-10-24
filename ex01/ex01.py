import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("car")
token = doc[0]
print(token.vector.shape)
# sum of first 20 values
s = sum(token.vector[:20])
print(float.as_integer_ratio(s))
