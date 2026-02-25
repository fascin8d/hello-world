# Voice Document Agent

Talk to any document or URL using a real-time voice agent powered by Pipecat + Claude.

## How It Works

1. You provide a PDF or URL
2. The agent extracts text, chunks it, and embeds it into a local vector store (ChromaDB)
3. A voice pipeline starts: you speak → Deepgram transcribes → Claude answers (searching the document via RAG) → Cartesia speaks back
4. Audio streams over Daily WebRTC — join from any browser

## Setup

### 1. Get API Keys

| Service    | Sign Up                              |
|------------|--------------------------------------|
| Anthropic  | https://console.anthropic.com        |
| Voyage AI  | https://dash.voyageai.com            |
| Deepgram   | https://console.deepgram.com         |
| Cartesia   | https://play.cartesia.ai             |
| Daily      | https://dashboard.daily.co           |

### 2. Configure Environment

```bash
cp .env.example .env
# Fill in your API keys in .env
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Discuss a PDF
python server.py --pdf path/to/document.pdf

# Discuss a web page
python server.py --url https://example.com/article
```

The agent prints a Daily room URL — open it in your browser and start talking.

## Architecture

```
PDF/URL → Extract → Chunk → Embed (Voyage AI) → ChromaDB

Mic → Deepgram STT → Claude (+ search_document tool) → Cartesia TTS → Speaker
```

## Configuration

Set `CARTESIA_VOICE_ID` in `.env` to change the voice. Browse voices at https://play.cartesia.ai.
