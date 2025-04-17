from fastapi import FastAPI
import random

app = FastAPI()

quotes = [
    "Believe in yourself!",
    "Every day is a second chance.",
    "Never stop learning.",
    "You are stronger than you think."
]

@app.get("/quote")
def get_quote():
    """Return a random quote."""
    return {"quote": random.choice(quotes)}