from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

from server.logger import logger
from server.modules.load_vectorstore import load_vectorstore

import os

router = APIRouter()


# -----------------------------
# Upload & Analyze Medical Reports
# -----------------------------
@router.post("/analyze_report/")
async def analyze_report(files: list[UploadFile] = File(...)):
    try:
        logger.info(f"Received {len(files)} medical report(s)")

        if not files:
            return JSONResponse(
                status_code=400,
                content={"error": "No files uploaded"}
            )

        # -----------------------------
        # STEP 1: Store + Vectorize PDFs
        # -----------------------------
        logger.info("Processing medical reports...")

        load_vectorstore(files)

        # -----------------------------
        # STEP 2: Response
        # -----------------------------
        return JSONResponse(
            status_code=200,
            content={
                "message": "Reports processed successfully",
                "files_processed": len(files),
                "status": "success"
            }
        )

    except Exception as e:
        logger.exception("Error analyzing medical report")

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "message": "Failed to analyze report"
            }
        )