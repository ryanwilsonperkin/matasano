from convert import base64_to_bytes
from vignere import auto_decrypt

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        in_file = open(sys.argv[1])
    else:
        in_file = sys.stdin

    base64_str = in_file.read().replace('\n', '')
    bytes = base64_to_bytes(base64_str)
    decrypted, key = auto_decrypt(bytes, 2, 40, 10)
    print 'KEY: {0}'.format(str(key))
    print 'DECRYPTED:\n{0}'.format(str(decrypted))
