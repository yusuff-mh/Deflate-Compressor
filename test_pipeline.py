import os
from main import compress

def run_test():
    test_filename = "test_input.txt"
    
    # We use a repetitive string to ensure LZ77 finds "Matches" 
    # and doesn't just output "Literals"
    test_data = b"abracadabraabracadabra"
    
    print("=== Step 1: Creating Test File ===")
    with open(test_filename, "wb") as f:
        f.write(test_data)
    print(f"Wrote {len(test_data)} bytes to '{test_filename}'")
    print(f"Raw data: {test_data}\n")
    
    print("=== Step 2: Running Compressor Pipeline ===")
    try:
        # This will call load_bytes -> lz77_compress -> symbolize_deflate
        symbols = compress(test_filename)
        
        print(f"Success! Generated {len(symbols)} symbols.\n")
        
        print("=== Step 3: Inspecting Symbol Stream ===")
        for i, sym in enumerate(symbols):
            if sym[0] == "LIT":
                # Display the byte character for easier debugging
                print(f"[{i:02d}] {sym} -> Literal '{chr(sym[1])}'")
            elif sym[0] == "LEN":
                print(f"[{i:02d}] {sym} -> Length")
            elif sym[0] == "DIST":
                print(f"[{i:02d}] {sym} -> Distance")
            elif sym[0] == "EOB":
                print(f"[{i:02d}] {sym} -> End of Block")
                
    except Exception as e:
        print(f"Error during compression: {e}")
        
    finally:
        # Clean up the test file
        if os.path.exists(test_filename):
            os.remove(test_filename)
            print(f"\nCleaned up '{test_filename}'.")

if __name__ == "__main__":
    run_test()