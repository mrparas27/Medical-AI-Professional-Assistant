from server.logger import logger
from typing import Dict, List
import re


class MedicalReportAnalyzer:
    """
    AI-powered medical report analyzer (rule-based + LLM-ready structure)

    NOTE:
    - This does NOT provide medical diagnosis
    - It only explains medical terms in simple language
    """

    def __init__(self):
        logger.info("Medical Report Analyzer initialized")

    # -----------------------------
    # Extract key values from text
    # -----------------------------
    def extract_values(self, text: str) -> Dict[str, str]:
        """
        Extract common medical values from report text
        (simple regex-based extraction)
        """

        try:
            patterns = {
                "glucose": r"(glucose|sugar)\s*[:\-]?\s*(\d+)",
                "hemoglobin": r"(hemoglobin|hb)\s*[:\-]?\s*(\d+\.?\d*)",
                "cholesterol": r"(cholesterol)\s*[:\-]?\s*(\d+)",
                "vitamin_d": r"(vitamin d)\s*[:\-]?\s*(\d+)",
            }

            results = {}

            for key, pattern in patterns.items():
                match = re.search(pattern, text.lower())
                if match:
                    results[key] = match.group(2)

            return results

        except Exception as e:
            logger.error(f"Error extracting values: {e}")
            return {}

    # -----------------------------
    # Simple interpretation logic
    # -----------------------------
    def analyze_values(self, values: Dict[str, str]) -> Dict[str, str]:
        """
        Convert numbers into simple human explanation
        """

        analysis = {}

        try:
            # Glucose
            if "glucose" in values:
                glucose = float(values["glucose"])
                if glucose > 140:
                    analysis["glucose"] = "High blood sugar detected (above normal range)"
                elif glucose < 70:
                    analysis["glucose"] = "Low blood sugar detected"
                else:
                    analysis["glucose"] = "Normal blood sugar level"

            # Hemoglobin
            if "hemoglobin" in values:
                hb = float(values["hemoglobin"])
                if hb < 12:
                    analysis["hemoglobin"] = "Low hemoglobin (possible anemia)"
                else:
                    analysis["hemoglobin"] = "Normal hemoglobin level"

            # Cholesterol
            if "cholesterol" in values:
                chol = float(values["cholesterol"])
                if chol > 200:
                    analysis["cholesterol"] = "High cholesterol level"
                else:
                    analysis["cholesterol"] = "Normal cholesterol level"

            # Vitamin D
            if "vitamin_d" in values:
                vd = float(values["vitamin_d"])
                if vd < 20:
                    analysis["vitamin_d"] = "Vitamin D deficiency detected"
                else:
                    analysis["vitamin_d"] = "Normal Vitamin D level"

            return analysis

        except Exception as e:
            logger.error(f"Error analyzing values: {e}")
            return {}

    # -----------------------------
    # Full report analysis pipeline
    # -----------------------------
    def analyze_report(self, text: str) -> Dict:
        """
        Main function → takes report text and returns insights
        """

        try:
            logger.info("Analyzing medical report...")

            values = self.extract_values(text)
            analysis = self.analyze_values(values)

            result = {
                "extracted_values": values,
                "analysis": analysis,
                "summary": self.generate_summary(analysis)
            }

            logger.info("Report analysis completed")

            return result

        except Exception as e:
            logger.exception("Report analysis failed")
            return {
                "error": str(e)
            }

    # -----------------------------
    # Human readable summary
    # -----------------------------
    def generate_summary(self, analysis: Dict[str, str]) -> str:
        """
        Convert analysis into readable explanation
        """

        if not analysis:
            return "No significant medical issues detected in the report."

        summary = "Medical Report Summary:\n"

        for key, value in analysis.items():
            summary += f"- {key.capitalize()}: {value}\n"

        return summary


# Global instance
report_analyzer = MedicalReportAnalyzer()