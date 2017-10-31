#!/usr/bin/env python3

"""
From F(1) = 1, F(2) = 1, F(n) = F(n-1) + F(n-2),
we see that F(3) is even, F(4), F(5) are odd, and F(6) is even,
since even = odd + odd and odd = evev + odd. Thus the even
Fibonacci numbers occur at F(n) where n % 3 == 0. We see if we can
express an even F(n) in terms of earlier even Fibonacci numbers.

F(n) = F(n-1) + F(n-2) = 2 F(n-2) + F(n-3) = 3 F(n-3) + 2 F(n-4)
= 3 F(n-3) + 2 F(n-5) + 2 F(n-6) = 4 F(n-3) - F(n-4) + F(n-5) + 2 F(n-6)
= 4 F(n-3) + F(n-6)
"""


if __name__ == "__main__":
    INCLUSIVE_UPPER_BOUND = 4_000_000
    s = 0
    Fn6, Fn3 = 2, 8
    while Fn6 <= INCLUSIVE_UPPER_BOUND:
        s, Fn6, Fn3 = s+Fn6, Fn3, Fn6 + 4 * Fn3
    print(s)
