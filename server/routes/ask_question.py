from dotenv import load_dotenv
from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

import os
from pathlib import Path

from ..logger import logger

# Load env variables from server/.env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

router = APIRouter()


# Custom Retriever - will be imported when needed


@router.post("/ask/")
async def ask_question(question: str = Form(...)):
    try:
        # Lazy imports for heavy libraries
        from pinecone import Pinecone
        from sentence_transformers import SentenceTransformer
        from langchain_core.documents import Document
        from langchain_core.retrievers import BaseRetriever
        from typing import List
        from ..modules.llm import get_llm_chain
        from ..modules.query_handers import query_chain
        
        # Define custom retriever
        class SimpleRetriever(BaseRetriever):
            def __init__(self, documents: List[Document]):
                super().__init__()
                self._docs = documents

            def _get_relevant_documents(self, query: str) -> List[Document]:
                return self._docs
        
        logger.info(f"User query received: {question}")

        # -----------------------------
        # ENV VARIABLES
        # -----------------------------
        api_key = os.getenv("PINECONE_API_KEY")
        index_name = os.getenv("PINECONE_INDEX_NAME")

        if not api_key or not index_name:
            logger.error("Missing Pinecone config")
            return JSONResponse(
                status_code=500,
                content={"error": "Pinecone not configured"}
            )

        # -----------------------------
        # PINECONE INIT
        # -----------------------------
        pc = Pinecone(api_key=api_key)
        index = pc.Index(index_name)

        # -----------------------------
        # EMBEDDING MODEL
        # -----------------------------
        embed_model = SentenceTransformer("all-MiniLM-L6-v2")

        query_vector = embed_model.encode(question).tolist()

        # -----------------------------
        # VECTOR SEARCH
        # -----------------------------
        results = index.query(
            vector=query_vector,
            top_k=3,
            include_metadata=True
        )

        matches = results.get("matches", [])

        # -----------------------------
        # CONVERT TO DOCUMENTS
        # -----------------------------
        docs = []
        sources = []

        for match in matches:
            metadata = match.get("metadata", {})

            docs.append(
                Document(
                    page_content=metadata.get("text", ""),
                    metadata=metadata
                )
            )

            sources.append(metadata.get("source", ""))

        # -----------------------------
        # RETRIEVER + LLM CHAIN
        # -----------------------------
        retriever = SimpleRetriever(docs)

        chain = get_llm_chain(retriever)
        result = query_chain(chain, question)

        # Add sources
        result["sources"] = list(set(sources))  # remove duplicates

        logger.info("Query processed successfully")

        return JSONResponse(
            status_code=200,
            content=result
        )

    except Exception as e:
        logger.exception("Error processing question")

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )