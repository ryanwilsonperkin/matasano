from convert import ascii_to_bytes, bytes_to_hex, bytes_to_ascii
from xor import xor_bytes

def encrypt(clear, seq):
    quotient, remainder = divmod(len(clear), len(seq))
    seq_repeated = seq * quotient + seq[:remainder]
    return xor_bytes(clear, seq_repeated)

def rotate(s, offset):
    return s[offset:] + s[:offset]

if __name__ == "__main__":
    import sys
    offset = 0
    key = ascii_to_bytes(sys.argv[1])
    for line in sys.stdin:
        clear = ascii_to_bytes(line)
        cipher = encrypt(clear, rotate(key, offset))
        offset = (offset - len(clear) / len(key)) % len(key)
        print bytes_to_hex(cipher)
