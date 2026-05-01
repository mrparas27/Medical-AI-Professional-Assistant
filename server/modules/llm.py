from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

# =========================
# ENV
# =========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# =========================
# RAG CHAIN BUILDER
# =========================
def get_llm_chain(retriever):
    """
    Build RAG chain using Groq + LangChain LCEL
    """

    if not GROQ_API_KEY:
        raise ValueError("❌ GROQ_API_KEY not found in .env")

    # -------------------------
    # LLM (UPDATED MODEL FIX)
    # -------------------------
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant",  # ✅ updated correct parameter
        temperature=0
    )

    # -------------------------
    # PROMPT
    # -------------------------
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are MediBot, an AI assistant for medical document understanding.

You ONLY use the provided context.

-----------------------------------
Context:
{context}

Question:
{question}
-----------------------------------

Rules:
- Be clear and simple
- Be factual
- If answer not found say:
  "I'm sorry, but I couldn't find relevant information in the provided documents."
- Never hallucinate
- Never give medical diagnosis or treatment

Answer:
"""
    )

    # -------------------------
    # RAG CHAIN (LCEL)
    # -------------------------
    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain