from typing import List
from pydantic import BaseModel

class Menu(BaseModel):
    title: str
    description: str
    usage: str
    endpoint1: str
    endpoint2: str
    result: str

class Tokenizer(BaseModel):
    original_text: str
    encoded_text: List[int] | List[List[int]]
    token_length: int
