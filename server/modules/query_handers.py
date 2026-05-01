from ..logger import logger


def query_chain(chain, user_input: str):
    """
    Executes LCEL / RAG chain safely and returns structured response
    """

    try:
        logger.debug(f"Running LLM chain for input: {user_input}")

        # -----------------------------
        # Invoke chain
        # -----------------------------
        result = chain.invoke(user_input)

        # -----------------------------
        # Normalize output
        # -----------------------------
        if isinstance(result, dict):
            response_text = (
                result.get("answer")
                or result.get("response")
                or str(result)
            )
        else:
            response_text = str(result)

        response = {
            "response": response_text,
            "sources": []  # populated in ask_question route
        }

        logger.debug(f"Chain response generated successfully")

        return response

    except Exception as e:
        logger.exception("Error in query_chain execution")

        return {
            "response": "Sorry, I couldn't process your request right now.",
            "sources": [],
            "error": str(e)
        }