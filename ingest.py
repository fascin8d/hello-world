"""Document ingestion: extract text, chunk, embed with Voyage AI, store in ChromaDB."""

import os

import chromadb
import requests
import voyageai
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "voyage-3-lite"
BATCH_SIZE = 128


def extract_text_from_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_text_from_url(url: str) -> str:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    return soup.get_text(separator="\n", strip=True)


def chunk_text(text: str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    return splitter.split_text(text)


def ingest(source: str) -> tuple[chromadb.Collection, voyageai.Client]:
    """Ingest a PDF or URL into ChromaDB. Returns (collection, voyage_client)."""

    if source.startswith("http://") or source.startswith("https://"):
        print(f"Fetching URL: {source}")
        text = extract_text_from_url(source)
    elif source.endswith(".pdf"):
        print(f"Reading PDF: {source}")
        text = extract_text_from_pdf(source)
    else:
        raise ValueError(f"Unsupported source: {source} (provide a URL or .pdf path)")

    print(f"Extracted {len(text)} characters")

    chunks = chunk_text(text)
    print(f"Split into {len(chunks)} chunks")

    # Embed with Voyage AI
    vo = voyageai.Client(api_key=os.getenv("VOYAGEAI_API_KEY"))
    all_embeddings = []
    for i in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[i : i + BATCH_SIZE]
        result = vo.embed(batch, model=EMBEDDING_MODEL, input_type="document")
        all_embeddings.extend(result.embeddings)

    # Store in ChromaDB (in-memory)
    db = chromadb.Client()
    try:
        db.delete_collection("document")
    except Exception:
        pass

    collection = db.create_collection(
        name="document",
        metadata={"hnsw:space": "cosine"},
    )
    collection.add(
        documents=chunks,
        embeddings=all_embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))],
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB")
    return collection, vo
