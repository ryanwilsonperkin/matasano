def xor_bytelist(list1, list2):
   """XOR two buffers.""" 
   return [int(e1) ^ int(e2) for e1, e2 in zip(list1, list2)] 

if __name__ == "__main__":
    import sys
    from convert import hex_to_bytelist, bytelist_to_hex
    if len(sys.argv) == 3:
        bytelist1 = hex_to_bytelist(sys.argv[1])
        bytelist2 = hex_to_bytelist(sys.argv[2])
        print bytelist_to_hex(xor_bytelist(bytelist1, bytelist2))
    else:
        print "error: missing hex strings"
        print "usage: python xor.py <hex_string> <hex_string>"
