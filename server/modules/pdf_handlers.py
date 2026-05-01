import shutil
from pathlib import Path
from typing import List

from fastapi import UploadFile
from server.logger import logger

# -----------------------------
# Base upload directory
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploaded_docs"


def save_uploaded_files(files: List[UploadFile]) -> List[str]:
    """
    Save uploaded files locally and return file paths
    """

    try:
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

        file_paths = []

        logger.info(f"Saving {len(files)} uploaded file(s)...")

        for file in files:
            try:
                file_name = file.filename

                # -----------------------------
                # Validation
                # -----------------------------
                if not file_name:
                    logger.warning("Skipping file with empty name")
                    continue

                file_name = file_name.strip().replace(" ", "_")

                save_path = UPLOAD_DIR / file_name

                # -----------------------------
                # Save file
                # -----------------------------
                with open(save_path, "wb") as buffer:
                    shutil.copyfileobj(file.file, buffer)

                file_paths.append(str(save_path))

                logger.info(f"Saved file: {file_name}")

            except Exception as file_error:
                logger.error(f"Failed to save file {file.filename}: {file_error}")

        logger.info("All files processed successfully")

        return file_paths

    except Exception as e:
        logger.exception("Error in save_uploaded_files")
        raise Exception(f"File saving failed: {str(e)}")