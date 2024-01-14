from fastapi import FastAPI
from pydantic import BaseModel
from src.utils import url_qa

app = FastAPI()

class Question(BaseModel):
    question: str
    url: str
    

@app.get("/")
def root():
    return {"Status": "Server running."}

@app.post("/ask")
def ask_question(question:Question):
    ans = url_qa(
        url=question.url,
        question=question.question
    )
    return ans
