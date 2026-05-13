from bit_io import BitReader
from huffman_logic import get_canonical_map
from symbolizing import LENGTH_CODES, DISTANCE_CODES

def decompress_logic(data):
    reader = BitReader(data)
    l_bw, d_bw = reader.read_bits(4), reader.read_bits(4)
    
    lit_lens = [reader.read_bits(l_bw) for _ in range(286)]
    dist_lens = [reader.read_bits(d_bw) for _ in range(30)]
    
    # Reverse map: Code -> Symbol
    lit_codes = {v: k for k, v in get_canonical_map(lit_lens).items()}
    dist_codes = {v: k for k, v in get_canonical_map(dist_lens).items()}
    
    output = bytearray()
    while True:
        curr = ""
        while curr not in lit_codes:
            b = reader.read_bit()
            if b is None: return output
            curr += b
        sym = lit_codes[curr]
        
        if 0 <= sym <= 255:
            output.append(sym)
        elif sym == 256: # EOB
            break
        else: # Match
            l_info = [c for c in LENGTH_CODES if c[0] == sym][0]
            length = l_info[2] + reader.read_bits(l_info[1])
            
            curr_d = ""
            while curr_d not in dist_codes: curr_d += reader.read_bit()
            d_sym = dist_codes[curr_d]
            d_info = [c for c in DISTANCE_CODES if c[0] == d_sym][0]
            dist = d_info[2] + reader.read_bits(d_info[1])
            
            # 2.5 Overlapping copy byte-by-byte
            for _ in range(length):
                output.append(output[-dist])
    return output