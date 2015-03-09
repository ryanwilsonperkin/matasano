from convert import hex_to_bytelist, bytelist_to_hex, bytelist_to_str
from single_byte_xor import candidates

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    candidate_list = []
    with open(input_file) as f:
        for line in f:
            line = line[:-1] if line.endswith('\n') else line
            cipher = hex_to_bytelist(line)
            top_candidate = candidates(cipher)[0]
            candidate_list.append(top_candidate)
    candidate_list.sort(reverse=True, key=lambda x: x.ranking)
    top_candidate = candidate_list[0]
    print "CIPHER: {0}".format(bytelist_to_hex(top_candidate.cipher))
    print "CLEAR: {0}".format(bytelist_to_hex(top_candidate.clear))
    print "DECODED: {0}".format(bytelist_to_str(top_candidate.clear))
    print "XOR Byte: {0}".format(top_candidate.key)
