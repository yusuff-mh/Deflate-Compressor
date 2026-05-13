import math
from bit_io import BitWriter

def get_bw(lengths):
    """Section 5.3: floor(log2(M)) + 1"""
    m = max(lengths) if lengths else 0
    return 0 if m == 0 else math.floor(math.log2(m)) + 1

def generate_compressed_data(events, lit_lengths, dist_lengths, lit_codes, dist_codes):
    writer = BitWriter()
    l_bw = get_bw(lit_lengths)
    d_bw = get_bw(dist_lengths)
    
    # Header fields
    writer.write_bits(l_bw, 4)
    writer.write_bits(d_bw, 4)
    for l in lit_lengths: writer.write_bits(l, l_bw)
    for l in dist_lengths: writer.write_bits(l, d_bw)
    
    # Payload
    for ev in events:
        if ev[0] == "LIT":
            writer.write_raw_string(lit_codes[ev[1]])
        elif ev[0] == "LEN":
            writer.write_raw_string(lit_codes[ev[1]])
            if ev[2] > 0: writer.write_bits(ev[3], ev[2])
        elif ev[0] == "DIST":
            writer.write_raw_string(dist_codes[ev[1]])
            if ev[2] > 0: writer.write_bits(ev[3], ev[2])
        elif ev[0] == "EOB":
            writer.write_raw_string(lit_codes[256])
            
    return writer.get_bytes()