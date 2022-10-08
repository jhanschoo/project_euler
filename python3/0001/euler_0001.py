#!/usr/bin/env python3

def sum_divisible_upto(target, d):
    n = target // d
    s = d * n * (n + 1) // 2
    return s

if __name__ == "__main__":
    target = 999
    answer = sum_divisible_upto(target, 3) + sum_divisible_upto(target, 5) - sum_divisible_upto(target, 3 * 5)
    print(answer)
