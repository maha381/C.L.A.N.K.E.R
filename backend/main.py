from fastapi import FastAPI
from pathlib import Path
from pydantic import BaseModel
from api.chat import orchastration
from api import chat 


app = FastAPI()


@app.post("/chat")
def root():
    for chunk in orchastration():
        yield chunk



