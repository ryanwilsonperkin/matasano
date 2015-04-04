from convert import hex_to_bytes, bytes_to_hex
from detect import rank, Candidate
from xor import xor_bytes

def candidates(cipher):
    candidates = [] 
    for byte in range(0,256):
        clear = xor_bytes(cipher, [byte] * len(cipher))
        ranking = rank(clear)
        candidates.append(Candidate(byte, cipher, clear, ranking))
    return sorted(candidates, reverse=True, key=lambda x: x.ranking)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        input_str = sys.argv[1]
    else:
        input_str = sys.stdin.read()
    cipher = hex_to_bytes(input_str)
    top_candidate = candidates(cipher)[0]
    print "CIPHER: {0}".format(bytes_to_hex(top_candidate.cipher))
    print "CLEAR: {0}".format(bytes_to_hex(top_candidate.clear))
    print "DECODED: {0}".format(str(top_candidate.clear))
    print "XOR Byte: {0}".format(top_candidate.key)
