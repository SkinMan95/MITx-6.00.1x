def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    while b:
        a, b = b, a % b
    return a

print(gcdIter(3,5))
print(gcdIter(3,6))
print(gcdIter(3,9))
