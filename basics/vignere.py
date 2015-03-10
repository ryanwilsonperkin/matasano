from convert import str_to_bytelist, bytelist_to_str, split_bytelist
from hamming import avg_distance
from xor import xor_bytelist
from single_byte_xor import candidates

def encrypt(clear, key):
    key = key_generator(key)
    key_repeated = [key.next() for c in clear]
    return xor_bytelist(clear, key_repeated)

def decrypt(cipher, key):
    return encrypt(cipher, key)

def key_generator(key):
    while True:
        for elem in key:
            yield elem

def keysize_candidates(bytelist, keysize_min, keysize_max, n_blocks):
    keysize_distance = dict()
    for keysize in range(keysize_min, keysize_max):
        first_block = bytelist[:keysize]
        blocks = split_bytelist(bytelist, keysize)[1:n_blocks+1]
        average = avg_distance(first_block, *blocks)
        keysize_distance[keysize] = average / keysize

    return sorted(keysize_distance.items(), key=lambda (x,y): y)

def auto_decrypt(bytelist, keysize_min, keysize_max, n_blocks):
    keysizes = keysize_candidates(bytelist, keysize_min, keysize_max, n_blocks)
    keysize, score = keysizes[0]

    blocks = split_bytelist(bytelist, keysize)
    transposed = zip(*blocks)

    key = map(lambda block: candidates(block)[0].key, transposed)
    return decrypt(bytelist, key), key
