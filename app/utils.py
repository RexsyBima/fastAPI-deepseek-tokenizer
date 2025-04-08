from typing import List
import transformers
from deepseek_tokenizer import ds_token
from .models import Tokenizer

CHAT_TOKENIZER_DIR = "./"
tokenizer = transformers.AutoTokenizer.from_pretrained( 
        CHAT_TOKENIZER_DIR, trust_remote_code=True
        )
# result = tokenizer.encode("Hello!")

def encode_text(data: str) -> Tokenizer:
    encoded = ds_token.encode(data)
    return Tokenizer(
        original_text=data, encoded_text=encoded, token_length=len(encoded)
    )
