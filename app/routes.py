from app import app, tokenizer, encode_text
from .model import Tokenizer
from fastapi import status
from pydantic import BaseModel

class TokenizerInput(BaseModel):
    text: str

@app.get("/")
async def homepage():
    return {"message": "Hello World"}

@app.post("/encode_transformer", status_code=status.HTTP_200_OK, response_model=Tokenizer)
async def encode_transformer(input: TokenizerInput):
    encoded_text = tokenizer.encode(input.text)
    return Tokenizer(original_text=input.text, encoded_text=encoded_text, token_length=len(encoded_text))

@app.post("/encode", status_code=status.HTTP_200_OK, response_model=Tokenizer) # this encode transformer is actually the tiktoken
async def encode_tokenizer(input: TokenizerInput):
    encoded_text = tokenizer.encode(input.text)
    return Tokenizer(original_text=input.text, encoded_text=encoded_text, token_length=len(encoded_text))
