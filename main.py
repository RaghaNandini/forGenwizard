from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import hashlib

app = FastAPI()


# Function to generate SHA256 token
def generate(text):
    return hashlib.sha256(text.encode()).hexdigest()


# Pydantic model
class TextInput(BaseModel):
    text: str


# Webpage endpoint
@app.get("/", response_class=HTMLResponse)
def welcome():
    return """
    <html>
    <head>
        <title>Welcome</title>
        <style>
            body{
                background-color:#111;
                color:white;
                font-family:Arial;
                text-align:center;
                padding-top:120px;
            }
            h1{
                color:#00ffcc;
                font-size:40px;
            }
            p{
                font-size:18px;
            }
        </style>
    </head>

    <body>

        <h1>Welcome to the webpage, Baina Ragha Nandini!</h1>

        <p>"The only way to do great work is to love what you do." – Steve Jobs</p>

        <h2>Containerized Python API</h2>

        <p>This application exposes a JSON API using FastAPI.</p>

    </body>
    </html>
    """


# API endpoint
@app.post("/generate")
def generate_token(data: TextInput):
    text = data.text
    token = generate(text)
    return {"checksum": token}
