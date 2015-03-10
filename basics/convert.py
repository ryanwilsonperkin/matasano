HEX_CHARS = '0123456789abcdef'
B64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def str_to_bytes(ascii_str):
    """Convert an ascii string to array of integer values."""
    return bytearray(ascii_str)

def bytes_to_str(bytes):
    """Convert array of integers into ascii string."""
    return ''.join(chr(b) for b in bytes)

def hex_to_int(h):
    """Get int value of hex character."""
    return HEX_CHARS.index(h)

def hex_to_bytes(hex_str):
    """Convert a hex string to array of integer values."""
    bytes = bytearray()
    if len(hex_str) % 2 == 1:
        hex_str = '0' + hex_str
    for upper_hex, lower_hex in map(''.join, zip(*[iter(hex_str)]*2)):
        upper_nibble = hex_to_int(upper_hex) 
        lower_nibble = hex_to_int(lower_hex) 
        bytes.append((upper_nibble << 4) | lower_nibble)
    return bytes

def int_to_hex(i):
    """Get hex character for integer value."""
    return HEX_CHARS[i]

def bytes_to_hex(bytes):
    """Convert array of integers into hex encoded string."""
    hex_str = ""
    for b in bytes:
        hex_str += int_to_hex(b >> 4)
        hex_str += int_to_hex(b & 15)
    return hex_str

def int_to_base64(i):
    """Get base 64 encoding of integer."""
    return B64_CHARS[i]

def base64_to_int(b):
    """Get int value of base64 character."""
    return B64_CHARS.index(b)

def bytes_to_base64(bytes):
    """Convert array of integers into base 64 encoded string."""
    base64_str = ""
    for b1, b2, b3 in zip(*[iter(bytes)]*3):
        base64_str += int_to_base64(b1 >> 2)
        base64_str += int_to_base64(((b1 << 4) & 48) | (b2 >> 4))
        base64_str += int_to_base64(((b2 << 2) & 60) | (b3 >> 6))
        base64_str += int_to_base64(b3 & 63)
    if len(bytes) % 3 == 1:
        b = bytes[-1]
        base64_str += int_to_base64(b >> 2)
        base64_str += int_to_base64((b << 4) & 48)
        base64_str += "=="
    elif len(bytes) % 3 == 2:
        b1, b2 = bytes[-2:]
        base64_str += int_to_base64(b1 >> 2)
        base64_str += int_to_base64(((b1 << 4) & 48) | (b2 >> 4))
        base64_str += int_to_base64((b2 << 2) & 60)
        base64_str += "="
    return base64_str

def base64_to_bytes(base64_str):
    """Convert base 64 encoded string into an array of integers."""
    bytes = bytearray()
    n_padding = base64_str.count('=')
    base64_str = base64_str.rstrip('=')
    for c1, c2, c3, c4 in zip(*[iter(base64_str)]*4):
        i1, i2, i3, i4 = map(base64_to_int, [c1, c2, c3, c4])
        bytes.append((i1 << 2) | (i2 >> 4))
        bytes.append(((i2 << 4) & 255) | (i3 >> 2))
        bytes.append(((i3 << 6) & 255) | i4)

    if n_padding == 1:
        c1, c2, c3 = base64_str[-3:]
        i1, i2, i3 = map(base64_to_int, [c1, c2, c3])
        bytes.append((i1 << 2) | (i2 >> 4))
        bytes.append(((i2 << 4) & 255) | (i3 >> 2))
    elif n_padding == 2:
        c1, c2 = base64_str[-2:]
        i1, i2 = map(base64_to_int, [c1, c2])
        bytes.append((i1 << 2) | (i2 >> 4))
    elif n_padding != 0:
        raise ValueError('Invalid padding')

    return bytes

def split_bytes(bytes, n):
    """Split a bytes into n chunks. Drop trailing bytes."""
    return zip(*[iter(bytes)]*n)

