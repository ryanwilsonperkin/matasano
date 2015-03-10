def byte_distance(b1, b2):
    return bin(b1 ^ b2).count('1')

def distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('lists must be of equal length')
    return sum(byte_distance(b1, b2) for b1, b2 in zip(list1, list2))

def avg_distance(list1, list2, *lists):
    distance_sum = distance(list1, list2)
    n_lists = 1
    for l in lists:
        distance_sum += distance(list1, l)
        n_lists += 1
    return float(distance_sum) / float(n_lists)
