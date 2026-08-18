```
services:
  qdrant: -> service or container name
    image: qdrant/qdrant -> Create the container from the qdrant/qdrant Docker image.
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage
volumes:
  qdrant_data:
```
--------------------------------------------------------------------------------------------------------
```
image: qdrant/qdrant
```

essentially it is same idea as-
docker pull qdrant/qdrant
docker run qdrant/qdrant

--------------------------------------------------------------------------------------------------------
```
"6333:6333"
```

```
HOST_PORT : CONTAINER_PORT
Your computer
localhost:6333
       │
       ▼
Qdrant container
port 6333
```
Application runs on computer can access : http://localhost:6333


--------------------------------------------------------------------------------------------------------
```
volumes:
    - qdrant_data:/qdrant/storage
```

```
Docker volume : Container path
qdrant_data
     │
     ▼
/qdrant/storage
```
Qdrant stores its database data in: /qdrant/storage
Docker mounts the persistent volume qdrant_data there.

--------------------------------------------------------------------------------------------------------
```
volumes:
  qdrant_data:
```
This declares docker volume

"Create/manage a persistent Docker volume called qdrant_data."
--------------------------------------------------------------------------------------------------------
```
services
    → What containers should Compose run?

image
    → Which Docker image should the container use?

ports
    → How do I expose container ports to my machine?

volumes
    → Where should persistent data live?

top-level volumes
    → Declare the Docker volumes Compose should manage.
```
--------------------------------------------------------------------------------------------------------
                 Your Mac
        ┌─────────────────────────┐
        │                         │
        │  localhost:6333         │
        │       │                 │
        │       │ port mapping    │
        │       ▼                 │
        │  ┌───────────────┐      │
        │  │ Qdrant        │      │
        │  │ container     │      │
        │  │               │      │
        │  │ :6333         │      │
        │  │               │      │
        │  │ /qdrant/      │      │
        │  │ storage       │      │
        │  └───────┬───────┘      │
        │          │              │
        │          ▼              │
        │   qdrant_data volume    │
        │                         │
        └─────────────────────────┘
--------------------------------------------------------------------------------------------------------