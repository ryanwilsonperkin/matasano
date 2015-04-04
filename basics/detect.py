from collections import namedtuple

COMMON_LETTERS = "ETAONRISHDL"
Candidate = namedtuple('Candidate', ['key', 'cipher', 'clear', 'ranking'])

def rank(bytes):
    count_space = bytes.count(bytearray(' '))
    count_upper = sum(bytes.count(bytearray(c)) for c in COMMON_LETTERS)
    count_lower = sum(bytes.count(bytearray(c.lower())) for c in COMMON_LETTERS)
    return count_space + count_upper + count_lower
