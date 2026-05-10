import sys
import os
from lz77 import lz77_compress


def load_bytes(filepath):
    with open(filepath, "rb") as f:
        return bytearray(f.read())


def compress(input_path):
    
    data = load_bytes(input_path)

    tokens = lz77_compress(data)

    ''' output is a list of tuples [
    ("Literal", 97),
    ("Literal", 98),
    ("Literal", 99),
    ("Match",   9, 3)
                                 ]
   '''

