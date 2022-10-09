#!/usr/bin/env python3

LIMIT = 20

if __name__ == "__main__":
    max_factors = {}
    for n in range(1, LIMIT + 1):
        factors = {}
        divisor = 2
        while n != 1:
            q, r = divmod(n, divisor)
            if r == 0:
                factors[divisor] = factors.get(divisor, 0) + 1
                n = q
            else:
                divisor += 1
        for divisor, count in factors.items():
            max_factors[divisor] = max(max_factors.get(divisor, 0), count)
    res = 1
    for divisor, count in max_factors.items():
        res *= divisor ** count
    print(res)