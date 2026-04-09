# Token Generator API

This project creates a simple FastAPI service that generates a SHA256 checksum token from input text.

## Run the API

uvicorn main:app --reload

## API Endpoints

GET /

Returns welcome message.

POST /generate

Input:
{
"text": "hello"
}

Output:
{
"checksum": "<generated sha256 token>"
}

## API Documentation

/docs