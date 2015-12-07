#!/usr/bin/python3

# https://projecteuler.net/problem=119
# https://www.hackerrank.com/contests/projecteuler/challenges/euler119

# Use log based comparison

import math
from collections import OrderedDict

def generateInterestingNumbers(limit):
    ans = []
    for base in range(2,1000):
        for pow in range(2, 110):
            num = base ** pow
            if num > limit:
                continue
            s = sum([int(c) for c in str(num)])
            if s == base:
                ans.append(num)
    return sorted(ans)

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(int(n % b))
        n = int(n//b)
    return ''.join(str(x) for x in digits[::-1])

def solveProjectEuler():
    #calculate for more numbers and sort them to get the 30th number in the sequence
    limit = 10 ** 100
    print( generateInterestingNumbers(limit)[29])


def solveHackerRank():
    B = int(input())
    ans = generateInterestingNumbers(10**100)
    print(ans)
    R = []
    for n in ans:
        R.append(numberToBase(n, B))

    print (' '.join(str(x) for x in R))


#solveProjectEuler()
solveHackerRank()
