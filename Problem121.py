#!/usr/bin/python3

# https://projecteuler.net/problem=121
# https://www.hackerrank.com/contests/projecteuler/challenges/euler121

# This problem, a series of independent events, can be solved by an ordinary generating function for the numerators of the respective probabilities. The nth coefficients of (x+1)(x+2)(x+3)…(x+15) are the sum of the products taken n at a time. We are only concerned with a winning scenario, which, for this problem, would be selecting 8 or more blue disks. Therefore, only the top eight coefficients are required.
#
# What’s left is to take the reciprocal of the sum of the eight coefficients divided by (n+1)!.
#
# Example: for n=7, the equation is (x+1)(x+2)(x+3)(x+4)(x+5)(x+6)(x+7) because we keep adding a red disk after each turn leaving 1 blue disk and 7 red disks for a total of 8 disks by the end of the game. This equation expands to:
# x7 + 28x6 + 322x5 + 1960x4 + 6769x3 + 13132x2 + 13068x + 5040.
# A winning scenario is selecting the blue disk 4 or more times (7 times out of 7 tries, 6 out of 7, 5 out of 7 or 4 out of 7) with the respective sum of the coefficients 1 + 28 + 322 + 1960 = 2311. The probability of winning is 2311/8! = 2311/40320. The prize fund would have to be the reciprocal of the winning probability, 40320/2311 ≈ £17.

import math
from collections import OrderedDict

from math import factorial

def solve(n):
    r = (n-1) // 2
    p = [1] + [0]*r
    print(p)
    for k in range(n+1):
        for i in range(r, 0, -1):
            p[i] += k * p[i-1]

    print(p)
    return factorial(n+1) // sum(p)

def solveProjectEuler():
    n = 7
    print( "For", n, "turns, max prize fund =", solve(n))    #calculate for more numbers and sort them to get the 30th number in the sequence


def solveHackerRank():
    T = int(input())
    while T:
        T -= 1
        N = int(input())
        print(solve(N))


solveProjectEuler()
#solveHackerRank()
