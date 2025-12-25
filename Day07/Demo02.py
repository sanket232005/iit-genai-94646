from langchain_openai import OpenAIEmbeddings
import numpy as np

def cosine_similarity(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

embed_model = OpenAIEmbeddings(
    model = "text-embedding-nomic-embed-text-v1.5",
    base_url="http://127.0.0.1:1234/v1",
    api_key = "api_key",
    check_embedding_ctx_length = False
)

sentences = [
    "I love football ,",
    "Soccer is my favorite sports .",
    "Messi Talk In spanish"
]

embeddings = embed_model.embed_documents(sentences)

for embed_vect in embeddings:
    print("Len : ", len(embed_vect), "-->" , embed_vect[:4])

print("Sentences 1 & 2 Similarity :",cosine_similarity(embeddings[0],embeddings[1]))    
print("Sentences 1 & 3 Similarity :",cosine_similarity(embeddings[0],embeddings[2]))    


