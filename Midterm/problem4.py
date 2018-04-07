def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    i = 2
    s = 1
    while s < k:
        s, i = s+i, i+1

    return s == k

for i in range(1, 16):
    print(i, is_triangular(i))
    
