from convert import base64_to_bytelist, bytelist_to_str
from hamming import avg_distance
from vignere import decrypt
from single_byte_xor import candidates

def split_list(bytelist, n):
    return zip(*[iter(bytelist)]*n)

def keysize_candidates(bytelist, keysize_min, keysize_max, n_blocks):
    keysize_distance = dict()
    for keysize in range(keysize_min, keysize_max):
        first_block = bytelist[:keysize]
        blocks = split_list(bytelist, keysize)[1:n_blocks+1]
        average = avg_distance(first_block, *blocks)
        keysize_distance[keysize] = average / keysize

    return sorted(keysize_distance.items(), key=lambda (x,y): y)

def transpose(blocks):
    return zip(*blocks)

def find_key(block):
    return candidates(block)[0].key

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        in_file = open(sys.argv[1])
    else:
        in_file = sys.stdin

    keysize_min = 2
    keysize_max = 40
    n_blocks = 10

    base64_str = in_file.read().replace('\n', '')
    bytelist = base64_to_bytelist(base64_str)
    keysizes = keysize_candidates(bytelist, keysize_min, keysize_max, n_blocks)
    keysize, score = keysizes[0]

    blocks = split_list(bytelist, keysize)
    blocks = transpose(blocks)

    key = map(find_key, blocks)
    decrypted = decrypt(bytelist, key)
    sys.stdout.write(bytelist_to_str(decrypted))
