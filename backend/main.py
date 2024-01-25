"""
RAG-QA backend logic.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from src.utils import get_answer

app = FastAPI()


class Question(BaseModel):
    """Question object used for RAG QA."""

    question: str
    pdf: str


@app.get("/")
def root():
    """Check status of backend server."""
    return {"status": "Server running."}


@app.post("/ask")
def ask_question(question: Question):
    """Run the QA RAG cycle on a document and return the answer."""
    ans = get_answer(pdf_string=question.pdf, question=question.question)
    return ans
