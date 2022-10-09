#!/usr/bin/env python3

import math

if __name__ == "__main__":
    sum_to_100 = (100 * 101) // 2 # 1000th triangle number
    square_of_sum = sum_to_100 ** 2
    sum_square_to_100 = (100 * 101 * 201) // 6 # 1000th pyramid number
    print(square_of_sum - sum_square_to_100)
