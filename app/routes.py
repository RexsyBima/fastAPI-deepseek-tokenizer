from pydantic import BaseModel
from .models import Menu, Tokenizer
from fastapi import status
from .utils import encode_text, tokenizer
from . import app


@app.get("/", response_model=Menu, status_code=status.HTTP_200_OK)
async def homepage():
    return Menu(title="deepseek tokenizer", description="simple fastapi server to calculate, and encode words into deepseek token", usage="""
   the text data must live in `text` header data, see the example there 

    http
### POST request
POST http://127.0.0.1:8000/encode_transformer HTTP/1.1
Content-Type: application/json
text: hello world dunia

    """, 
    endpoint1="/encode -> uses tokenizer to encode the text", 
    endpoint2="/encode_transformer -> uses transformers to encode the text", 
    result="""result will be a Tokenizer object with 3 atribute:
    original_text: str
    encoded_text: List[int] | List[List[int]]
    token_length: int
""")


class TokenizerInput(BaseModel):
    text : str

@app.post("/encode", status_code=status.HTTP_200_OK, response_model=Tokenizer)
async def encode_tokenizer(input_data: TokenizerInput):
    text = input_data.text
    assert isinstance(text, str), "text header is empty, please set it"
    data = encode_text(text)
    return data

@app.post("/encode_transformer", status_code=status.HTTP_200_OK, response_model=Tokenizer)
async def encode_transformer(input_data: TokenizerInput):
    text = input_data.text
    assert isinstance(text, str), "text header is empty, please set it"
    encoded_text = tokenizer.encode(text)
    return Tokenizer(original_text=text, encoded_text=encoded_text, token_length=len(encoded_text))
