import spacy

nlp = spacy.load("en_core_web_sm")

text = """Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. It is considered one of the Big Five companies in the U.S. information technology industry, along with Amazon, Google, Microsoft, and Facebook.
Apple was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976 to develop and sell Wozniak's Apple I personal computer, though Wayne sold his share back within 12 days. It was incorporated as Apple Computer, Inc., in January 1977, and sales of its computers, including the Apple I and Apple II, grew quickly."""

doc = nlp(text)
print("Named entities:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")

print("\nAmbiguous 'apple':")
text2 = "Paul eats an apple while watching a movie on his Apple device."
doc2 = nlp(text2)
for ent in doc2.ents:
    print(
        f"entity={ent.text!r}, start_char={ent.start_char}, "
        f"end_char={ent.end_char}, label={ent.label_}"
    )
