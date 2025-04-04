from fastapi import Request, Response
from .models import Tokenizer
from fastapi import status
from .utils import encode_text
from . import app


@app.get("/")
async def homepage():
    return "hello world"


@app.post("/encode", status_code=status.HTTP_200_OK, response_model=Tokenizer)
async def encode_tokenizer(request: Request):
    text = request.headers.get("text")
    assert isinstance(text, str)
    data = encode_text(text)
    return data
