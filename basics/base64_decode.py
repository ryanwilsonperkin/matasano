import sys
from convert import base64_to_bytes

if __name__ == "__main__":
    if len(sys.argv) == 2:
        base64_str = sys.argv[1]
    else:
        base64_str = sys.stdin.read()

    bytes = base64_to_bytes(base64_str)
    sys.stdout.write(str(bytes))
