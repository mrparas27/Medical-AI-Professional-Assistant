import logging
import os
from datetime import datetime


def setup_logger(name="MedicalAssistant"):
    """
    Creates a reusable logger for the project
    """

    logger = logging.getLogger(name)

    # Prevent duplicate logs
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG)

    # -----------------------
    # Console Handler
    # -----------------------
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # -----------------------
    # Log Format
    # -----------------------
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler.setFormatter(formatter)

    # Attach handler
    logger.addHandler(console_handler)

    return logger


# Global logger instance
logger = setup_logger()


# -----------------------
# Test Logs (remove later if you want clean logs)
# -----------------------
if __name__ == "__main__":
    logger.info("RAG logger initialized successfully")
    logger.debug("Debugging mode active")
    logger.error("An error occurred")
    logger.critical("Critical issue detected")