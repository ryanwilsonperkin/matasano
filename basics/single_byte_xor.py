from collections import namedtuple
from sys import argv
from convert import hex_to_bytes, bytes_to_hex
from xor import xor_bytes

COMMON_LETTERS = "ETAONRISHDL "
Candidate = namedtuple('Candidate', ['key', 'clear_text', 'ranking'])

def rank(s):
    return sum([s.count(c) + s.count(c.lower())  for c in COMMON_LETTERS])

def candidates(byte_list):
    candidates = [] 
    for byte in range(0,256):
        decoded = xor_bytes(byte_list, [byte] * len(byte_list))
        clear_text = ''.join(chr(b) for b in decoded)
        ranking = rank(clear_text)
        candidates.append(Candidate(byte, clear_text, ranking))

    return sorted(candidates, reverse=True, key=lambda x: x[2])

if __name__ == "__main__":
    input_str = argv[1]
    input_bytes = hex_to_bytes(input_str)
    top_candidate = candidates(input_bytes)[0]
    print "HEX: {0}".format(bytes_to_hex([ord(c) for c in top_candidate[1]]))
    print "ASCII: {0}".format(top_candidate.clear_text)
    print "XOR Byte: {0}".format(top_candidate.key)
