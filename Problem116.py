#!/usr/local/bin/python3

# https://projecteuler.net/problem=116
# https://www.hackerrank.com/contests/projecteuler/challenges/euler116

# Use log based comparison

import math
from collections import OrderedDict

def F(m, n):
    ways = [1] * m + [0] * (n-m+1)
    print(ways)
    for j in range(m, n+1):
        ways[j] += ways[j - 1] + ways[j - m]
    return ways[n] - 1

def solveProjectEuler():
    n = 50
    print( "Space size = " + str(n))
    ans = F(2, n) + F(3, n) + F(4, n)
    print("Number of ways to fill:" + str(ans))


def fill(row, tile):
    if row < tile:
        return 0
    if row == tile:
        return 1
    count = 0
    for i in range(row - tile + 1):
        count += 1 + fill(row - tile - i, tile)
    return count


def solveHackerRank():
    T = int(input())
    M = 1000000007
    while T:
        T -= 1
        n = int(input())
        count = 0
        for i in [2, 3, 4]:
            count += fill(n, i)
        print(count%M)

#solveProjectEuler()
solveHackerRank()
