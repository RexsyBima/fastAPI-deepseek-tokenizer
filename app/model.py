from pydantic import BaseModel

class Tokenizer(BaseModel):
        original_text: str
        encoded_text: list[int]
        token_length: int
