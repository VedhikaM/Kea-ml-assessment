from fastapi import FastAPI
from similarity import find_best_match

app = FastAPI()

@app.get("/")
def home():
    return {"message": "KeaBuilder ML Similarity API"}

@app.get("/match")
def match(query: str):
    result = find_best_match(query)
    return {
        "query": query,
        "best_match": result
    }
