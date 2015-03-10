import sys
from convert import bytes_to_base64, str_to_bytes

if __name__ == "__main__":
    if len(sys.argv) == 2:
        ascii_str = sys.argv[1]
    else:
        ascii_str = sys.stdin.read()

    bytes = str_to_bytes(ascii_str)
    sys.stdout.write(bytes_to_base64(bytes))
