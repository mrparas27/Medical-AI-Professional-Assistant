import os
import time
from pathlib import Path
from typing import List, Tuple

from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from PyPDF2 import PdfReader

from ..logger import logger

# Load env variables from server/.env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# =========================
# ENV VARIABLES
# =========================
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV", "us-east-1")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "medicalindex")

# =========================
# PATHS
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploaded_docs"
UPLOAD_DIR.mkdir(exist_ok=True)

# =========================
# GLOBALS (lazy load)
# =========================
_pc = None
_index = None
_embed_model = None


# =========================
# PINECONE INIT
# =========================
def _init_pinecone():
    global _pc, _index

    if _pc and _index:
        return _pc, _index

    if not PINECONE_API_KEY:
        raise ValueError("PINECONE_API_KEY missing in .env")

    logger.info("Initializing Pinecone...")

    _pc = Pinecone(api_key=PINECONE_API_KEY)

    existing_indexes = [i["name"] for i in _pc.list_indexes()]

    # ⚠️ FIX IMPORTANT: dimension must match embedding model = 384
    if PINECONE_INDEX_NAME not in existing_indexes:
        _pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region=PINECONE_ENV
            )
        )

        while not _pc.describe_index(PINECONE_INDEX_NAME).status["ready"]:
            time.sleep(1)

    _index = _pc.Index(PINECONE_INDEX_NAME)

    logger.info("Pinecone ready")
    return _pc, _index


# =========================
# EMBEDDING MODEL
# =========================
def _get_embed_model():
    global _embed_model

    if _embed_model is None:
        logger.info("Loading embedding model...")

        from sentence_transformers import SentenceTransformer

        _embed_model = SentenceTransformer("all-MiniLM-L6-v2")

        logger.info("Embedding model loaded")

    return _embed_model


# =========================
# TEXT SPLITTING
# =========================
def split_text(text: str, chunk_size: int = 500, overlap: int = 50):
    text = text.strip()
    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])

        if end == len(text):
            break

        start += chunk_size - overlap

    return chunks


# =========================
# PDF READER
# =========================
def extract_pdf_text(file_path: str) -> List[Tuple[int, str]]:
    reader = PdfReader(file_path)

    pages = []

    for i, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""

        pages.append((i, text))

    return pages


# =========================
# MAIN VECTORSTORE LOADER
# =========================
def load_vectorstore(uploaded_files):
    logger.info(f"Processing {len(uploaded_files)} files")

    _, index = _init_pinecone()
    embed_model = _get_embed_model()

    for file in uploaded_files:
        try:
            # Save file
            file_path = UPLOAD_DIR / file.filename

            with open(file_path, "wb") as f:
                f.write(file.file.read())

            logger.info(f"Saved: {file.filename}")

            # Extract text
            pages = extract_pdf_text(str(file_path))

            texts, metadata, ids = [], [], []

            for page_num, text in pages:
                chunks = split_text(text)

                for chunk_idx, chunk in enumerate(chunks):
                    texts.append(chunk)

                    metadata.append({
                        "source": file.filename,
                        "page": page_num,
                        "chunk": chunk_idx,
                        "text": chunk
                    })

                    ids.append(f"{file_path.stem}-{page_num}-{chunk_idx}")

            if not texts:
                logger.warning(f"No text found in {file.filename}")
                continue

            # Embeddings
            embeddings = embed_model.encode(texts)

            # ⚠️ FIX: Pinecone expects LIST OF FLOAT LISTS
            vectors = []
            for i in range(len(ids)):
                vectors.append({
                    "id": ids[i],
                    "values": embeddings[i].tolist() if hasattr(embeddings[i], "tolist") else list(embeddings[i]),
                    "metadata": metadata[i]
                })

            # Upload
            index.upsert(vectors=vectors)

            logger.info(f"Uploaded successfully: {file.filename}")

        except Exception as e:
            logger.exception(f"Upload failed for {file.filename}")
            raise e