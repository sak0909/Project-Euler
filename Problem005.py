#!/usr/local/bin/python3

# https://projecteuler.net/problem=5
# https://www.hackerrank.com/contests/projecteuler/challenges/euler005

# Its a LCM problem. LCM(a,b) can be obtained by a*b/GCD(a,b)

import math

from fractions import gcd
def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b//gcd(a,b)

T = int(input())
while T:
    T -= 1
    N = int(input())
    ans = 1;
    for i in range(1, N+1):
        ans = lcm(ans, i)
    print(ans)

