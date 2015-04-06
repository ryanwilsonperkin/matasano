def pad(bytes, block_size):
    """Pad byes to multiple of block_size using PKCS#7 padding."""
    if len(bytes) < block_size:
        pad = block_size - len(bytes)
    else:
        pad = block_size - (len(bytes) % block_size)
    print pad
    bytes.extend([pad] * pad)

