from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
GQA = pipeline(model = "Varshitha/flan-t5-large-finetune-medicine-v5")

class RequestBody(BaseModel):
    input: str

@app.post("/rb/")

def rb(body:RequestBody):
    result = GQA(body.input)
    return result
