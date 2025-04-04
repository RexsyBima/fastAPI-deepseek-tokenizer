from typing import List
from pydantic import BaseModel


class Tokenizer(BaseModel):
    original_text: str
    encoded_text: List[int] | List[List[int]]
    token_length: int
