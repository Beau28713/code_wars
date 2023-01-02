from collections import Counter

def scramble(s1, s2):
    one = Counter(s1)
    two = Counter(s2)

    return two <= one