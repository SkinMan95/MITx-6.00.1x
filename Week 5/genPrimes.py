def genPrimes():
    def is_prime(x):
        lim = x**.5
        i = 2
        r = True
        while i <= lim and r:
            r, i = x % i != 0, i+1

        return r

    i = 1
    while True:
        i += 1
        while not is_prime(i):
            i += 1
        yield i

primes = genPrimes()
print(type(primes))
for i in range(50):
    print(primes.__next__())
