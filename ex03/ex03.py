import spacy
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_md")
sentence = "laptop computer coffee tea water liquid dog cat kitty"
doc = nlp(sentence)
words = [token.text for token in doc]
vectors = [token.vector for token in doc]
sim = cosine_similarity(vectors)
plt.figure(figsize=(10, 8))
plt.imshow(sim, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(words)), words, rotation=45)
plt.yticks(range(len(words)), words)
plt.tight_layout()
plt.savefig('w3day05ex1_plot.png')
plt.close()
