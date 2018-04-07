def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    rep = {}
    for e in L:
        rep[e] = rep.get(e, 0) +1

    lar = None
    for e in rep.keys():
        if rep[e] % 2 != 0:
            lar = max(lar, e) if lar != None else e

    return lar

print(largest_odd_times([2,2,4,4]))
print(largest_odd_times([3,9,5,3,5,3]))
