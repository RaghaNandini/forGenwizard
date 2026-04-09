from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import hashlib

app = FastAPI()

def generate(text):
    return hashlib.sha256(text.encode()).hexdigest()

class TextInput(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def welcome():
    return """
    <html>
    <head>
        <title>Welcome</title>
        <style>
            body {
                font-family: Arial;
                background-color: #111;
                color: white;
                text-align: center;
                padding-top: 100px;
            }
            h1 { color: #00ffcc; }
            p { font-size:18px; }
        </style>
    </head>

    <body>
        <h1>Welcome to the webpage, Baina Ragha Nandini!</h1>
        <p>"The only way to do great work is to love what you do." – Steve Jobs</p>
        <h2>Containerized Python API</h2>
        <p>This API generates SHA256 tokens using FastAPI</p>
    </body>
    </html>
    """


@app.post("/generate")
def generate_token(data: TextInput):
    text = data.text
    token = generate(text)
    return {"checksum": token}
