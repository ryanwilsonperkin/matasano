from convert import ascii_to_bytes, bytes_to_hex
from xor import xor_bytes

def encrypt(clear, seq):
    quotient, remainder = divmod(len(clear), len(seq))
    seq_repeated = seq * quotient + seq[:remainder]
    return xor_bytes(clear, seq_repeated)

if __name__ == "__main__":
    import sys
    key = ascii_to_bytes(sys.argv[1])
    for line in sys.stdin:
        clear = ascii_to_bytes(line)
        cipher = encrypt(clear, key)
        print bytes_to_hex(cipher)
