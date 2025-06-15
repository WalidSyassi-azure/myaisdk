from fastapi import FastAPI
from pydantic import BaseModel
import myai  # your SDK module

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_ai(q: Question):
    return {"answer": myai.answer(q.question)}
