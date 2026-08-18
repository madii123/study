# Install required packages: pip install sentence-transformers qdrant-client
"""
                         ┌─────────────┐
                         │   Qdrant    │
                         │             │
Temporal text ─────────→ │ vector +    │
Kafka text ────────────→ │ metadata    │
Kubernetes text ───────→ │             │
                         └─────────────┘

Each Qdrant point contains:
id
vector → [384 numbers]
payload
   └── text → "Temporal is..."
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams
from sentence_transformers import SentenceTransformer

# model = SentenceTransformer("all-MiniLM-L6-v2")
# text = "Temporal is a workflow orchestration platform for durable execution."
# embedding = model.encode(text)

# print(text, len(embedding), embedding[:5])

# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# connect to local client
client = QdrantClient(url="http://localhost:6333")
COLLECTION_NAME = "my_documents"

# create collection
client.collection_exists(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)

# sample documents
documents = [
    "Temporal is a workflow orchestration platform for durable execution.",
    "Kafka is a distributed event streaming platform used to process messages.",
    "Kubernetes manages containerized applications and can restart unhealthy pods.",
]

# convert documents to vector
embeddings = model.encode(documents)

# store vector in Qdrant
points = []
l = len(documents)

for i in range(l):
    document, embedding = documents[i], embeddings[i]
    points.append(
        PointStruct(id=i, vector=embedding.tolist(), payload={"text": document})
    )

client.upsert(collection_name=COLLECTION_NAME, points=points)

print("Inserted documents", len(points))
