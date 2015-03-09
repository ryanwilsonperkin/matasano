from convert import ascii_to_bytelist, bytelist_to_hex, bytelist_to_str
from xor import xor_bytelist

def encrypt(clear, seq):
    quotient, remainder = divmod(len(clear), len(seq))
    seq_repeated = seq * quotient + seq[:remainder]
    return xor_bytelist(clear, seq_repeated)

def rotate(s, offset):
    return s[offset:] + s[:offset]

if __name__ == "__main__":
    import sys
    offset = 0
    key = ascii_to_bytelist(sys.argv[1])
    for line in sys.stdin:
        clear = ascii_to_bytelist(line)
        cipher = encrypt(clear, rotate(key, offset))
        offset = (offset - len(clear) / len(key)) % len(key)
        print bytelist_to_hex(cipher)
