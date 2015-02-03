HEX_CHARS = '0123456789abcdef'
B64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def hex_to_int(h):
    """Get int value of hex character."""
    return HEX_CHARS.index(h)

def hex_to_bytes(hex_str):
    """Convert a hex string to array of integer values."""
    byte_list = []
    if len(hex_str) % 2 == 1:
        hex_str = '0' + hex_str
    for upper_hex, lower_hex in map(''.join, zip(*[iter(hex_str)]*2)):
        upper_nibble = hex_char_to_int(upper_hex) 
        lower_nibble = hex_char_to_int(lower_hex) 
        byte_list.append((upper_nibble << 4) | lower_nibble)
    return byte_list

def int_to_hex(i):
    """Get hex character for integer value."""
    return HEX_CHARS[i]

def bytes_to_hex(byte_list):
    """Convert array of integers into hex encoded string."""
    hex_str = ""
    for b in byte_list:
        hex_str += int_to_hex(b >> 4)
        hex_str += int_to_hex(b & 15)
    return hex_str

def int_to_base64(i):
    """Get base 64 encoding of integer."""
    return B64_CHARS[i]

def bytes_to_base64(byte_list):
    """Convert array of integers into base 64 encoded string."""
    base64_str = ""
    for b1, b2, b3 in zip(*[iter(byte_list)]*3):
        base64_str += int_to_base64(b1 >> 2)
        base64_str += int_to_base64(((b1 << 4) & 48) | (b2 >> 4))
        base64_str += int_to_base64(((b2 << 2) & 60) | (b3 >> 6))
        base64_str += int_to_base64(b3 & 63)
    if len(byte_list) % 3 == 1:
        b = byte_list[-1]
        base64_str += int_to_base64(b >> 2)
        base64_str += int_to_base64((b << 4) & 48)
        base64_str += "=="
    elif len(byte_list) % 3 == 2:
        b1, b2 = byte_list[-2:]
        base64_str += int_to_base64(b1 >> 2)
        base64_str += int_to_base64(((b1 << 4) & 48) | (b2 >> 4))
        base64_str += int_to_base64((b2 << 2) & 60)
        base64_str += "="
    return base64_str

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        hex_str = sys.argv[1]
        byte_list = hex_to_bytes(hex_str)
        print bytes_to_base64(byte_list)
    else:
        print "error: missing hex string"
        print "usage: python hex_to_b64.py <hex_string>"
        sys.exit(1)
