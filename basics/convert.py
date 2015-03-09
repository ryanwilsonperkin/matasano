HEX_CHARS = '0123456789abcdef'
B64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def str_to_bytelist(ascii_str):
    """Convert an ascii string to array of integer values."""
    return [ord(c) for c in ascii_str]

def bytelist_to_str(bytelist):
    """Convert array of integers into ascii string."""
    return ''.join(chr(b) for b in bytelist)

def hex_to_int(h):
    """Get int value of hex character."""
    return HEX_CHARS.index(h)

def hex_to_bytelist(hex_str):
    """Convert a hex string to array of integer values."""
    bytelist = []
    if len(hex_str) % 2 == 1:
        hex_str = '0' + hex_str
    for upper_hex, lower_hex in map(''.join, zip(*[iter(hex_str)]*2)):
        upper_nibble = hex_to_int(upper_hex) 
        lower_nibble = hex_to_int(lower_hex) 
        bytelist.append((upper_nibble << 4) | lower_nibble)
    return bytelist

def int_to_hex(i):
    """Get hex character for integer value."""
    return HEX_CHARS[i]

def bytelist_to_hex(bytelist):
    """Convert array of integers into hex encoded string."""
    hex_str = ""
    for b in bytelist:
        hex_str += int_to_hex(b >> 4)
        hex_str += int_to_hex(b & 15)
    return hex_str

def int_to_base64(i):
    """Get base 64 encoding of integer."""
    return B64_CHARS[i]

def bytelist_to_base64(bytelist):
    """Convert array of integers into base 64 encoded string."""
    base64_str = ""
    for b1, b2, b3 in zip(*[iter(bytelist)]*3):
        base64_str += int_to_base64(b1 >> 2)
        base64_str += int_to_base64(((b1 << 4) & 48) | (b2 >> 4))
        base64_str += int_to_base64(((b2 << 2) & 60) | (b3 >> 6))
        base64_str += int_to_base64(b3 & 63)
    if len(bytelist) % 3 == 1:
        b = bytelist[-1]
        base64_str += int_to_base64(b >> 2)
        base64_str += int_to_base64((b << 4) & 48)
        base64_str += "=="
    elif len(bytelist) % 3 == 2:
        b1, b2 = bytelist[-2:]
        base64_str += int_to_base64(b1 >> 2)
        base64_str += int_to_base64(((b1 << 4) & 48) | (b2 >> 4))
        base64_str += int_to_base64((b2 << 2) & 60)
        base64_str += "="
    return base64_str
