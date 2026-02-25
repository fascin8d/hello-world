# Voice Document Agent — Implementation Plan

## Overview
A Pipecat voice agent you can talk to about any document (PDF, text) or URL.
You load a document, the agent ingests it, and you have a real-time voice
conversation about its contents using RAG via function calling.

---

## Architecture

```
                        ┌─────────────────────────────────┐
                        │         Document Ingestion       │
                        │                                  │
  PDF / URL / Text ───► │  Extract → Chunk → Embed → Store │
                        │                   (OpenAI)  (Chroma)│
                        └──────────────┬──────────────────┘
                                       │ vector store ready
                                       ▼
┌──────────────────────────────────────────────────────────────┐
│                    Pipecat Voice Pipeline                     │
│                                                              │
│  Mic ─► [Transport In] ─► [STT] ─► [User Aggregator]        │
│                                          │                   │
│                                          ▼                   │
│                                       [LLM]                  │
│                                    (w/ function calling)     │
│                                     │          │             │
│                              search_doc()   normal reply     │
│                                  │              │            │
│                                  ▼              ▼            │
│                            [ChromaDB]       [TTS] ─► Speaker │
│                              │                               │
│                              └──► result back to LLM ──►TTS  │
│                                                              │
│  [Assistant Aggregator] ◄── context saved                    │
└──────────────────────────────────────────────────────────────┘
```

---

## Tech Stack

| Component        | Choice                  | Why                                    |
|------------------|-------------------------|----------------------------------------|
| Framework        | Pipecat (`pipecat-ai`)  | Purpose-built for voice agents         |
| STT              | Deepgram                | Fast, accurate, streaming              |
| LLM              | OpenAI `gpt-4o`         | Best function-calling support          |
| TTS              | Cartesia                | Ultra-low latency voice synthesis      |
| Embeddings       | OpenAI `text-embedding-3-small` | Cheap, good quality           |
| Vector Store     | ChromaDB (local)        | Zero-config, no external service       |
| Doc Parsing      | PyPDF2 + BeautifulSoup  | PDF + URL extraction                   |
| Text Splitting   | LangChain splitters     | Robust recursive chunking              |
| Transport        | Daily WebRTC            | Production-quality audio, free tier    |
| VAD              | Silero                  | Accurate voice activity detection      |

---

## File Structure

```
hello-world/
├── PLAN.md                     # This file
├── requirements.txt            # Python dependencies
├── .env.example                # Required API keys template
├── README.md                   # Setup & usage instructions
├── server.py                   # Main entry point — starts the bot
├── ingest.py                   # Document/URL ingestion pipeline
├── rag.py                      # Vector store search + function schema
└── bot.py                      # Pipecat pipeline definition
```

---

## Implementation Steps

### Step 1: Project Setup
- Create `requirements.txt` with all dependencies
- Create `.env.example` with required API key placeholders
- Initialize Python project structure

### Step 2: Document Ingestion (`ingest.py`)
- `ingest_pdf(path)` — extract text from PDF using PyPDF2
- `ingest_url(url)` — fetch URL, extract text with BeautifulSoup
- `ingest_text(text)` — accept raw text
- Chunk text using `RecursiveCharacterTextSplitter` (1000 chars, 200 overlap)
- Embed chunks with OpenAI embeddings
- Store in ChromaDB persistent collection
- Return the collection for querying

### Step 3: RAG Function Calling (`rag.py`)
- Define `search_document` FunctionSchema for Pipecat:
  ```
  name: "search_document"
  description: "Search the loaded document for information relevant to the user's question"
  properties: { query: string }
  ```
- Implement `search_document_handler(params)`:
  - Query ChromaDB with the user's query
  - Return top 3-5 relevant chunks as context
  - Set `run_llm=True` so the LLM generates a response using the retrieved context
- Register the function on the LLM service

### Step 4: Voice Pipeline (`bot.py`)
- Configure services:
  - Deepgram STT (streaming)
  - OpenAI LLM with system prompt:
    > "You are a voice assistant that helps users understand and discuss a document.
    > Use the search_document function to find relevant information before answering.
    > Keep responses concise and conversational (2-3 sentences).
    > If you can't find the answer in the document, say so."
  - Cartesia TTS
  - Silero VAD
- Build pipeline:
  ```
  transport.input() → STT → user_aggregator → LLM → TTS → transport.output() → assistant_aggregator
  ```
- Register function calling handlers
- Add TTS filler on function call start ("Let me check the document...")

### Step 5: Server Entry Point (`server.py`)
- Parse CLI args: `--pdf <path>` or `--url <url>`
- Run document ingestion
- Create Daily room (or use provided room URL)
- Start the Pipecat pipeline
- Print the room URL for the user to join

### Step 6: README with setup instructions
- API key setup (Deepgram, OpenAI, Cartesia, Daily)
- Install dependencies
- Run examples:
  ```bash
  python server.py --pdf my-document.pdf
  python server.py --url https://example.com/article
  ```

---

## API Keys Required

| Service   | Free Tier                | Sign Up                              |
|-----------|--------------------------|--------------------------------------|
| Deepgram  | $200 free credit         | https://console.deepgram.com         |
| OpenAI    | Pay-as-you-go            | https://platform.openai.com          |
| Cartesia  | Free tier available      | https://play.cartesia.ai             |
| Daily     | 10,000 min/month free    | https://dashboard.daily.co           |

---

## Future Upgrades (Supabase Path)
- Replace ChromaDB with Supabase pgvector for persistent, multi-user storage
- Add Supabase Auth for per-user document collections
- Use Supabase Storage for document file management
- Add Supabase Edge Functions for serverless deployment
