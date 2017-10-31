#!/usr/bin/env python3

import math

if __name__ == "__main__":
    NUMBER = 600_851_475_143
    candidate_factor = 3
    largest_prime_factor = 1
    sqrt_n = math.sqrt(NUMBER)

    # handle common small primes
    if NUMBER % 2 == 0:
        largest_prime_factor = 2
        while NUMBER % 2 == 0:
            NUMBER /= 2
    while candidate_factor <= sqrt_n:
        if NUMBER % candidate_factor == 0:
            largest_prime_factor = candidate_factor
            while NUMBER % candidate_factor == 0:
                NUMBER /= candidate_factor
        candidate_factor += 2
    print(largest_prime_factor)
