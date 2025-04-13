from fastapi import FastAPI
import transformers

app = FastAPI()

chat_tokenizer_dir = "./"

tokenizer = transformers.AutoTokenizer.from_pretrained( 
        chat_tokenizer_dir, trust_remote_code=True
        )

def encode_text(data: str) -> str:
        encoded_text = tokenizer.encode(data)
        return encoded_text

from . import routes
