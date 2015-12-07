#!/usr/bin/python3

# https://projecteuler.net/problem=25
# https://www.hackerrank.com/contests/projecteuler/challenges/euler25

#

import math
from collections import OrderedDict

def generateFib(limit):
    ans = []
    ans.append(str(1))
    ans.append(str(1))
    i = 2
    while 1:
        n = str(int(ans[i-1]) + int(ans[i-2]))
        ans.append(n)
        if len(n) >= limit:
            break;
        i += 1
    return ans


def solveProjectEuler():
    print(len(generateFib(1000)))


def solveHackerRank():
    F = generateFib(5000)
    T = int(input())
    while T:
        T -= 1
        N = int(input())
        for i, val in enumerate(F):
            if len(val) == N:
                print(i+1)
                break



#solveProjectEuler()
solveHackerRank()
