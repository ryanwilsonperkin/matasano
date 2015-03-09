def byte_distance(b1, b2):
    return bin(b1 ^ b2).count('1')

def distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('lists must be of equal length')
    return sum(byte_distance(b1, b2) for b1, b2 in zip(list1, list2))
