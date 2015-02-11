from sys import argv
from convert import hex_to_bytes, bytes_to_hex
from xor import xor_bytes

COMMON_LETTERS = "ETAONRISHDL "

def rank(s):
    return sum([s.count(c) + s.count(c.lower())  for c in COMMON_LETTERS])

if __name__ == "__main__":
    input_str = argv[1]
    input_bytes = hex_to_bytes(input_str)

    candidates = [] 
    for byte in range(0,256):
        byte_arr = [byte for i in xrange(len(input_bytes))]
        clear_text = ''.join(chr(b) for b in xor_bytes(byte_arr, input_bytes))
        ranking = rank(clear_text)
        candidates.append((byte, clear_text, ranking))

    candidates.sort(reverse=True, key=lambda x: x[2])

    top_candidate = candidates[0]
    print "HEX: {0}".format(bytes_to_hex([ord(c) for c in top_candidate[1]]))
    print "ASCII: {0}".format(top_candidate[1])
    print "XOR Byte: {0}".format(top_candidate[0])
