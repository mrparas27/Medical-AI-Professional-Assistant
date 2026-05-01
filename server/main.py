from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.upload_pdfs import router as upload_router
from .routes.ask_question import router as ask_router
from .logger import logger

from pathlib import Path
import os

# Load env variables from server/.env
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

logger.info("Starting Medical Assistant API...")
logger.info(f"PINECONE_API_KEY loaded: {bool(os.getenv('PINECONE_API_KEY'))}")
logger.info(f"PINECONE_INDEX_NAME loaded: {os.getenv('PINECONE_INDEX_NAME')}")

# FastAPI app
app = FastAPI(
    title="Medical Assistant API",
    description="AI Medical Assistant using RAG + LLM",
    version="2.0"
)

# ---------------------------
# CORS CONFIG
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # frontend access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

logger.info("CORS middleware configured")

# ---------------------------
# ROUTES
# ---------------------------
app.include_router(upload_router, prefix="/api")
app.include_router(ask_router, prefix="/api")

logger.info("Routers loaded successfully")

# ---------------------------
# HEALTH CHECK ROUTE
# ---------------------------
@app.get("/")
def root():
    return {
        "message": "🩺 Medical Assistant API Running",
        "status": "active",
        "docs": "/docs"
    }

# ---------------------------
# STARTUP EVENT
# ---------------------------
@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Server started at http://127.0.0.1:8000")