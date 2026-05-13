# main.py
import sys
import os
from lz77 import lz77_compress
from symbolizing import symbolize_deflate  
# Importing the logic for the new stages
from custom_header_and_payload import generate_compressed_data
from decompression import decompress_logic

def load_bytes(filepath):
    with open(filepath, "rb") as f:
        return bytearray(f.read())

def compress(input_path):
    data = load_bytes(input_path)
    tokens = lz77_compress(data)
    deflate_symbols = symbolize_deflate(tokens)
    
    # We add the End of Block marker (Section 5.5)
    deflate_symbols.append(("EOB", 256))
    return deflate_symbols

if __name__ == "__main__":
    # Requirement 8: Terminal Argument Handling
    if len(sys.argv) < 3:
        print("Usage: python main.py -c <file> OR python main.py -d <file>")
        sys.exit(1)
        
    mode, path = sys.argv[1], sys.argv[2]
    
    if mode == "-c":
        symbols = compress(path)
        # Assuming partner's huffman_logic provides lengths and codes
        # result = generate_compressed_data(symbols, lit_lens, dist_lens, lit_map, dist_map)
        # with open(path + ".sdfl", "wb") as f: f.write(result)
        pass 
        
    elif mode == "-d":
        data = load_bytes(path)
        original = decompress_logic(data)
        with open(path.replace(".sdfl", ""), "wb") as f:
            f.write(original)
