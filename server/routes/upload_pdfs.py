from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from typing import List

from ..modules.load_vectorstore import load_vectorstore
from ..logger import logger

router = APIRouter()


# -----------------------------
# Upload PDFs Endpoint
# -----------------------------
@router.post("/upload_pdfs/")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    try:
        logger.info("📥 Upload request received")

        # -----------------------------
        # Validation
        # -----------------------------
        if not files or len(files) == 0:
            logger.warning("No files provided in request")
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": "No files uploaded"
                }
            )

        logger.info(f"Processing {len(files)} file(s)")

        # -----------------------------
        # Process PDFs → Vector DB
        # -----------------------------
        load_vectorstore(files)

        logger.info("✅ Documents successfully added to vectorstore")

        # -----------------------------
        # Response
        # -----------------------------
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Files processed and vectorstore updated",
                "files_count": len(files)
            }
        )

    except Exception as e:
        logger.exception("❌ Error during PDF upload")

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": str(e),
                "message": "Failed to process uploaded files"
            }
        )