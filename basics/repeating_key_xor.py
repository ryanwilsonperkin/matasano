from convert import ascii_to_bytelist, bytelist_to_hex, bytelist_to_str
from xor import xor_bytelist

def encrypt(clear, key):
    key = key_generator(key)
    key_repeated = [key.next() for c in clear]
    return xor_bytelist(clear, key_repeated)

def key_generator(key):
    while True:
        for elem in key:
            yield elem

if __name__ == "__main__":
    import sys
    offset = 0
    key = ascii_to_bytelist(sys.argv[1])
    if len(sys.argv) == 3:
        in_file = open(sys.argv[2])
    else:
        in_file = sys.stdin
    for line in in_file:
        clear = ascii_to_bytelist(line)
        cipher = encrypt(clear, key)
        print bytelist_to_hex(cipher)
