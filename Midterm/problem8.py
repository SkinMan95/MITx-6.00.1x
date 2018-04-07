def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    t, k = L[0], len(L)
    if len(L) == 1:
        return lambda x: t
    else:
        return lambda x: t*(x**(k-1)) + general_poly(L[1:])(x)

print(general_poly([1, 2, 3, 4])(20))
