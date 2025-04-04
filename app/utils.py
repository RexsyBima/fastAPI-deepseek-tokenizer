from typing import List
from deepseek_tokenizer import ds_token
from .models import Tokenizer


def encode_text(data: str) -> Tokenizer:
    encoded = ds_token.encode(data)
    return Tokenizer(
        original_text=data, encoded_text=encoded, token_length=len(encoded)
    )
