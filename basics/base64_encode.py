import sys
from convert import bytelist_to_base64, str_to_bytelist

if __name__ == "__main__":
    if len(sys.argv) == 2:
        ascii_str = sys.argv[1]
    else:
        ascii_str = sys.stdin.read()

    bytelist = str_to_bytelist(ascii_str)
    sys.stdout.write(bytelist_to_base64(bytelist))
