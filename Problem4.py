#!/usr/local/bin/python3

# https://projecteuler.net/problem=4
# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

# Brute force/Go greedy from high values to low

import math


def find_max_palindrome(_max=999):
    max_palindrome = 0
    a = 999
    while a > 99:
        b = 999
        while b >= a:
            prod = a*b
            if prod > _max:
                b -= 1
                continue
            if prod > max_palindrome and str(prod)==(str(prod)[::-1]):
                max_palindrome = prod
            b -= 1
        a -= 1
    return max_palindrome

T = int(input())
while T:
    T -= 1
    N = int(input())
    print(find_max_palindrome(N))

