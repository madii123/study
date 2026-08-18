Pre-requiste:

```
1. install a smalles model of ollama:

      curl -fsSL https://ollama.com/install.sh | sh
      ollama list 
      ollama pull smollm2:135m
      ollama run smollm2:135m

2. Run a vector db
   we have docker-compose.yaml
   Do docker compose up

3. ingest
   python3 ingest.py

4. Query-ask question
   python3 query.py
```
----------------------------------------------------------------------------------------------------------------------------------------------------
OVERALL FLOW

```
Documents
   ↓
Chunk
   ↓
Embedding model
   ↓
Qdrant
   ↓
Question
   ↓
Embedding
   ↓
Top-K chunks
   ↓
Llama via Ollama
   ↓
Answer
```

----------------------------------------------------------------------------------------------------------------------------------------------------
INGESTION:

```
Documents -> embedding models -> vectors -> qdrant
```
----------------------------------------------------------------------------------------------------------------------------------------------------
RETRIEVAL:
                         
```
User Question
     │
     ▼
Embedding Model
     │
     ▼
Question Vector
     │
     ▼
Qdrant
     │
     ▼
Top-K Relevant Documents
     │
     │
     └────────────────┐
                      ▼
                 ┌─────────┐
Question ───────►│  Llama  │
                 └────┬────┘
                      │
                      ▼
                    Answer
```