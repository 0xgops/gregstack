from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is alive!"}

@app.get("/scores")
def get_scores():
    with open("scores.json") as f:
        data = json.load(f)
    return {"scores": data}