from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

# Create FastAPI app
app = FastAPI(
    title="Token Generator API",
    description="API to generate SHA256 checksum from input text",
    version="1.0.0"
)

# Function to generate SHA256 token
def generate(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Pydantic model for request body
class TextInput(BaseModel):
    text: str

# Welcome endpoint
@app.get("/", summary="Welcome API")
def welcome():
    return {"message": "Welcome to Token Generator API - Created by RaghaNandini"}

# Endpoint to generate checksum
@app.post(
    "/generate",
    summary="Generate Token",
    description="Generates SHA256 checksum for the provided text input"
)
def generate_token(data: TextInput):
    text = data.text
    token = generate(text)
    return {"checksum": token}