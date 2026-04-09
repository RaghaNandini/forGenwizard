from fastapi import FastAPI
import hashlib

app = FastAPI()

def generate(text):
    return hashlib.sha256(text.encode()).hexdigest()

@app.get("/")
def welcome():
    return {"message": "Welcome to Token Generator API"}

# endpoint to generate checksum from text
@app.post("/generate")
def generate_token(data: dict):
    text = data["text"]
    token = generate(text)
    return {"checksum": token}
