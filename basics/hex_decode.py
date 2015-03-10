import sys
from convert import bytes_to_str, hex_to_bytes

if __name__ == "__main__":
    if len(sys.argv) == 2:
        hex_str = sys.argv[1]
    else:
        hex_str = sys.stdin.read()

    bytes = hex_to_bytes(hex_str)
    sys.stdout.write(bytes_to_str(bytes))
