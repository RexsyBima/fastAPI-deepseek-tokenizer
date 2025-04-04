from app import app
from uvicorn import run
import sys
print(sys.argv)
port = int(sys.argv[1])
assert isinstance(port, int), "please provide port, for an example port of 8080, python3 run.py 8080"
run(app, port=port)
