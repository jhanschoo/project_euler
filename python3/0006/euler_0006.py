#!/usr/bin/env python3

# Wikipedia gives p_n < n(ln n + ln ln n) for n > 5

import math

N = 10001
SIEVE_SIZE = math.floor(N * (math.log(N) + math.log(math.log(N))))

if __name__ == "__main__":
    sieve = [True] * SIEVE_SIZE
    sieve[0] = sieve[1] = False
    primes_seen = 1
    for i in range(3, SIEVE_SIZE, 2):
        if sieve[i]:
            primes_seen += 1
            if primes_seen == N:
                print(i)
                break
            for j in range(2 * i, SIEVE_SIZE, i):
                sieve[j] = False