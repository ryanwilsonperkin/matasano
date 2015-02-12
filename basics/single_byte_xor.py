from collections import namedtuple
from sys import argv
from convert import hex_to_bytes, bytes_to_hex
from xor import xor_bytes

COMMON_LETTERS = "ETAONRISHDL"
Candidate = namedtuple('Candidate', ['key', 'cipher', 'clear', 'ranking'])

def rank(s):
    count_space = s.count(ord(' '))
    count_upper = sum(s.count(ord(c)) for c in COMMON_LETTERS)
    count_lower = sum(s.count(ord(c.lower())) for c in COMMON_LETTERS)
    return count_space + count_upper + count_lower

def candidates(cipher):
    candidates = [] 
    for byte in range(0,256):
        clear = xor_bytes(cipher, [byte] * len(cipher))
        ranking = rank(clear)
        candidates.append(Candidate(byte, cipher, clear, ranking))
    return sorted(candidates, reverse=True, key=lambda x: x.ranking)

if __name__ == "__main__":
    input_str = argv[1]
    cipher = hex_to_bytes(input_str)
    top_candidate = candidates(cipher)[0]
    print "CIPHER: {0}".format(bytes_to_hex(top_candidate.cipher))
    print "CLEAR: {0}".format(bytes_to_hex(top_candidate.clear))
    print "DECODED: {0}".format(''.join(chr(b) for b in top_candidate.clear))
    print "XOR Byte: {0}".format(top_candidate.key)
