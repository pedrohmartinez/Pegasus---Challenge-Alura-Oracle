from src.embeddings.embedder import (
    generate_embedding,
)

texto = """
Python é uma linguagem de programação.
"""

embedding = generate_embedding(texto)

print(type(embedding))
print(len(embedding))