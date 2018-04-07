def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    valid = len(L1) == len(L2)
    dic = {}
    if valid:
        for e in L1:
            dic[e] = dic.get(e, 0) +1

        for k in dic.keys():
            valid = valid and L2.count(k) == dic[k]

    if valid and len(L1) == 0:
        return (None, None, None)
    elif valid:
        lar, val = 0, None
        for k in dic.keys():
            if dic[k] > lar:
                lar, val = dic[k], k
        return (val, lar, type(val))
    else:
        return False

L1 = ['a', 'a', 'b']
L2 = ['a', 'b']
print(is_list_permutation(L1, L2))

L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1, L2))
