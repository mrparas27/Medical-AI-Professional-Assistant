from typing import Optional
from server.logger import logger

import os

# Optional: Google Translate fallback (lightweight)
try:
    from googletrans import Translator
    _translator = Translator()
except Exception:
    _translator = None
    logger.warning("googletrans not installed. Translation will be disabled.")


class LanguageTranslator:
    """
    Simple translation layer for Medical Assistant AI
    Supports: Hindi ↔ English (and other languages via googletrans)
    """

    def __init__(self):
        self.translator = _translator

    # -----------------------------
    # Detect language
    # -----------------------------
    def detect_language(self, text: str) -> Optional[str]:
        try:
            if not self.translator:
                return None

            return self.translator.detect(text).lang
        except Exception as e:
            logger.error(f"Language detection failed: {e}")
            return None

    # -----------------------------
    # Translate text
    # -----------------------------
    def translate(self, text: str, dest_lang: str = "en") -> str:
        """
        Translate input text to target language
        Default: English
        """

        try:
            if not self.translator:
                logger.warning("Translator not available, returning original text")
                return text

            if not text.strip():
                return text

            result = self.translator.translate(text, dest=dest_lang)

            logger.info(f"Translated text → {dest_lang}")

            return result.text

        except Exception as e:
            logger.exception("Translation failed")
            return text

    # -----------------------------
    # Auto translate (smart)
    # -----------------------------
    def auto_translate_to_english(self, text: str) -> str:
        """
        Automatically convert any language → English
        (Useful before sending to LLM)
        """
        try:
            lang = self.detect_language(text)

            if lang and lang != "en":
                return self.translate(text, "en")

            return text

        except Exception as e:
            logger.error(f"Auto translation failed: {e}")
            return text


# Global instance (import anywhere)
translator = LanguageTranslator()