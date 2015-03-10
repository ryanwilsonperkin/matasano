from Crypto.Cipher import AES
from convert import base64_to_bytes

def decrypt(bytes, key):
    cipher_text = str(bytes)
    key_str = str(key)
    decryptor = AES.new(key_str)
    clear_text = decryptor.decrypt(cipher_text)
    return bytearray(clear_text)

if __name__ == "__main__":
    import sys
    key = bytearray(sys.argv[1])
    if len(sys.argv) == 3:
        in_file = open(sys.argv)
    else:
        in_file = sys.stdin

    base64_str = in_file.read().replace('\n', '')
    bytes = base64_to_bytes(base64_str)
    decrypted = decrypt(bytes, key)
    sys.stdout.write(decrypted)
