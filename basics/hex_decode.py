import sys
from convert import bytelist_to_str, hex_to_bytelist

if __name__ == "__main__":
    if len(sys.argv) == 2:
        hex_str = sys.argv[1]
    else:
        hex_str = sys.stdin.read()

    bytelist = hex_to_bytelist(hex_str)
    sys.stdout.write(bytelist_to_str(bytelist))
