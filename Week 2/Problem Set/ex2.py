balance = 999999
annualInterestRate = 0.18

EPS = 1e-4

def check(b, i, fp) -> float:
    n = 12
    while n:
        b = (b - fp) * (1.0 + i)
        n -= 1
    return b

def main():
    hi = balance * (1+annualInterestRate/12.0)**12 / 12
    low = balance / 12.0
    found = False
    v = 0.0
    
    while not found and low < hi:
        mid = (hi+low) / 2
        v = check(balance, annualInterestRate/12.0, mid)
        print(hi, low, mid, v)
        found = abs(v) < EPS
        if not found:
            if v < 0:
                hi = mid
            else:
                low = mid
    print("Lowest Payment: %.2f" % mid)

main()
