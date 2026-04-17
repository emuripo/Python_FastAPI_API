# Technical Challenge: Build an AI-Ready Document Processing API with FastAPI

Design and implement a backend API using Python and FastAPI that simulates the core components of an AI-powered document processing system.

The API should be structured in a clean, scalable, and production-minded way, following good backend engineering practices. The system must be designed to support future integration with services such as Azure OpenAI, Azure AI Search, and Azure Blob Storage.

## What the solution should demonstrate

- Clear API design
- Request/response validation
- Separation of concerns
- Asynchronous processing where appropriate
- Extensibility for chunking, embeddings, and retrieval workflows

## Core capabilities

The system should allow users to:

- Upload or register documents
- Process documents into chunks
- Track processing status
- Retrieve processed chunks
- Perform a basic search over the processed content

You do not need to fully integrate external AI services, but your design should leave clear extension points for:

- Embedding generation
- Vector search
- Secret/configuration management
- Background processing pipelines

## Implementation focus

Focus on writing code that is:

- Easy to understand
- Easy to extend
- Realistic for a production AI backend

## Functional Requirements

### 1. Document Registration

Create an endpoint to register a document with:

- `title`
- `raw text content`

Each document should receive a unique ID and an initial status such as `uploaded`.

### 2. Document Processing

Create an endpoint to process a document.

Processing should:

- Split the document into chunks
- Store the chunks
- Update the processing status

You can implement a simple chunking strategy based on word count, but the code should be easy to replace later with a more advanced chunking approach.

### 3. Processing Status

Allow users to retrieve the current status of a document:

- `uploaded`
- `processing`
- `processed`
- `failed`

### 4. Chunk Retrieval

Allow users to retrieve the generated chunks for a given document.

### 5. Basic Search

Create an endpoint that accepts a query and returns matching chunks from processed documents.

This can be a simple keyword search for now, but the design should make it easy to replace with vector search later.

### 6. Health Check

Provide a simple health endpoint to confirm the API is running.

## Non-Functional Requirements

Your solution should also show:

- Clean folder structure
- Good naming
- Modular code
- Async-ready design
- Error handling
- Clear extension points for Azure integrations

## Bonus points

- Dependency injection
- Config management
- Background processing preparation
- Comments explaining future Azure/OpenAI integration points

## Expected Endpoints

### Health

- `GET /health`

### Documents

- `POST /documents`
- `GET /documents/{document_id}`
- `POST /documents/{document_id}/process`
- `GET /documents/{document_id}/status`
- `GET /documents/{document_id}/chunks`

### Search

- `POST /search`

## Suggested Request and Response Examples

### `POST /documents`

Request:

```json
{
  "title": "Azure RAG Notes",
  "content": "Azure OpenAI can be used for embeddings and answer generation..."
}
```

Response:

```json
{
  "id": "123e4567",
  "title": "Azure RAG Notes",
  "status": "uploaded"
}
```

### `POST /documents/{document_id}/process`

Response:

```json
{
  "document_id": "123e4567",
  "status": "processed",
  "chunks_created": 4
}
```

### `GET /documents/{document_id}/status`

Response:

```json
{
  "document_id": "123e4567",
  "status": "processed"
}
```

### `GET /documents/{document_id}/chunks`

Response:

```json
{
  "document_id": "123e4567",
  "chunks": [
    "Azure OpenAI can be used...",
    "Azure AI Search can store..."
  ]
}
```

### `POST /search`

Request:

```json
{
  "query": "Azure OpenAI"
}
```

Response:

```json
{
  "query": "Azure OpenAI",
  "results": [
    {
      "document_id": "123e4567",
      "chunk": "Azure OpenAI can be used..."
    }
  ]
}
```
# Project Structure 
app/
├── main.py
├── api/
│   └── routes/
│       ├── documents.py
│       └── search.py
├── schemas/
│   ├── document.py
│   └── search.py
├── services/
│   ├── document_service.py
│   ├── chunking_service.py
│   └── search_service.py
├── integrations/
│   ├── azure_openai_client.py
│   └── azure_search_client.py
├── db/
│   └── fake_db.py
└── core/
    └── config.py


routes	---> request
schemas ---> validation
services --->logic
repositories ---> DB
integrations ---> Azure / externals APIs 