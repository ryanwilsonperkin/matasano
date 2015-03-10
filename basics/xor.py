def xor_bytes(list1, list2):
   """XOR two buffers.""" 
   return [int(e1) ^ int(e2) for e1, e2 in zip(list1, list2)] 

if __name__ == "__main__":
    import sys
    from convert import hex_to_bytes, bytes_to_hex
    if len(sys.argv) == 3:
        bytes1 = hex_to_bytes(sys.argv[1])
        bytes2 = hex_to_bytes(sys.argv[2])
        print bytes_to_hex(xor_bytes(bytes1, bytes2))
    else:
        print "error: missing hex strings"
        print "usage: python xor.py <hex_string> <hex_string>"
