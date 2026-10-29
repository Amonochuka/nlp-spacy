import spacy
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

matplotlib.use("Agg")

nlp = spacy.load("en_core_web_md")
sentence = "laptop computer coffee tea water liquid dog cat kitty"
doc = nlp(sentence)

words = [token.text for token in doc]
vectors = [token.vector for token in doc]

similarities = cosine_similarity(vectors)

print("Words:", words)
print("Cosine similarities:")
for word, row in zip(words, similarities):
    print(word, " ".join(f"{value:.2f}" for value in row))

fig, ax = plt.subplots(figsize=(10, 8))
image = ax.imshow(similarities, cmap="hot", interpolation="nearest")
fig.colorbar(image, ax=ax)
ax.set_xticks(range(len(words)), words, rotation=45)
ax.set_yticks(range(len(words)), words)
ax.set_title("Pairwise cosine similarities")
fig.tight_layout()

output_path = Path(__file__).with_name("w3day05ex1_plot.png")
fig.savefig(output_path, dpi=150)
plt.close(fig)

print(f"Saved heatmap to {output_path}")
