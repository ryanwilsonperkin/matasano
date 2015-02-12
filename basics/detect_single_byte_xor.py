from sys import argv
from convert import hex_to_bytes, bytes_to_hex
from single_byte_xor import candidates

if __name__ == "__main__":
    input_file = argv[1]
    candidate_list = []
    with open(input_file) as f:
        for line in f:
            line = line[:-1] if line.endswith('\n') else line
            line_bytes = hex_to_bytes(line)
            candidate_list.extend(candidates(line_bytes))

    candidate_list.sort(reverse=True, key=lambda x: x.ranking)
    top_candidate = candidate_list[0]
    print "HEX: {0}".format(bytes_to_hex([ord(c) for c in top_candidate[1]]))
    print "ASCII: {0}".format(top_candidate.clear_text)
    print "XOR Byte: {0}".format(top_candidate.key)
