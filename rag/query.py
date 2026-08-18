from ollama import chat
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "my_documents"

model = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(url="http://localhost:6333")

question = "How can workflows survive worker failures?"

# Convert question into a vector
question_vector = model.encode(question).tolist()

# search in vector database
results = client.query_points(
    collection_name=COLLECTION_NAME,
    query=question_vector,
    limit=2,
).points


for result in results:
    print(result.score, result.payload["text"])

# extract retrieved contents
context = ",".join(result.payload["text"] for result in results)

response = chat(
    model="smollm2:135m",
    messages=[
        {
            "role": "user",
            "content": f"""
                Answer the question using only the provided context.
                Context: {context}
                Question: {question}
            """,
        }
    ],
)
print(response.message.content)
