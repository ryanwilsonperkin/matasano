from convert import hex_to_bytes, bytes_to_hex

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        in_file = open(sys.argv[1])
    else:
        in_file = sys.stdin
    candidate_list = []
    for line in in_file:
        line = line[:-1] if line.endswith('\n') else line
        cipher = hex_to_bytes(line)
        unique_blocks = set(zip(*[iter(cipher)]*16))
        candidate_list.append((cipher, len(unique_blocks)))
    candidate_list.sort(key=lambda (cipher, candidate): candidate)
    top_candidate = candidate_list[0]
    print bytes_to_hex(top_candidate[0])
