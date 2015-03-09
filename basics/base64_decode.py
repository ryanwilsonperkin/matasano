import sys
from convert import base64_to_bytelist, bytelist_to_str

if __name__ == "__main__":
    if len(sys.argv) == 2:
        base64_str = sys.argv[1]
    else:
        base64_str = sys.stdin.read()

    bytelist = base64_to_bytelist(base64_str)
    sys.stdout.write(bytelist_to_str(bytelist))
