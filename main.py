# main.py
import sys
import os
from lz77 import lz77_compress
from symbolizing import symbolize_deflate  

def load_bytes(filepath):
    with open(filepath, "rb") as f:
        return bytearray(f.read())

def compress(input_path):
    data = load_bytes(input_path)
    tokens = lz77_compress(data)
    
    # 3. Symbolize the LZ77 tokens for Deflate
    deflate_symbols = symbolize_deflate(tokens)
    
    return deflate_symbols

if __name__ == "__main__":
    # Example usage:
    # file_to_compress = "sample.txt"
    # if os.path.exists(file_to_compress):
    #     symbols = compress(file_to_compress)
    #     print(symbols)
    pass