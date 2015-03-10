from convert import str_to_bytes, bytes_to_str, split_bytes
from hamming import avg_distance
from xor import xor_bytes
from single_byte_xor import candidates

def encrypt(clear, key):
    key = key_generator(key)
    key_repeated = [key.next() for c in clear]
    return xor_bytes(clear, key_repeated)

def decrypt(cipher, key):
    return encrypt(cipher, key)

def key_generator(key):
    while True:
        for elem in key:
            yield elem

def keysize_candidates(bytes, keysize_min, keysize_max, n_blocks):
    keysize_distance = dict()
    for keysize in range(keysize_min, keysize_max):
        first_block = bytes[:keysize]
        blocks = split_bytes(bytes, keysize)[1:n_blocks+1]
        average = avg_distance(first_block, *blocks)
        keysize_distance[keysize] = average / keysize

    return sorted(keysize_distance.items(), key=lambda (x,y): y)

def auto_decrypt(bytes, keysize_min, keysize_max, n_blocks):
    keysizes = keysize_candidates(bytes, keysize_min, keysize_max, n_blocks)
    keysize, score = keysizes[0]

    blocks = split_bytes(bytes, keysize)
    transposed = zip(*blocks)

    key = map(lambda block: candidates(block)[0].key, transposed)
    return decrypt(bytes, key), key
