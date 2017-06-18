#!/usr/bin/python3

# https://projecteuler.net/problem=124
# https://www.hackerrank.com/contests/projecteuler/challenges/euler124

import math
from collections import OrderedDict

from math import factorial

def pe124(L):
    E = [[1,_] for _ in range(L)]
    for i in range(2, L):
        if E[i][0] == 1:
            for j in range(i, L, i):
                E[j][0] *= i

    return E




def solveProjectEuler():
    L, k = 100000+1, 10000
    print ("kth element in sorted list of radicals", sorted(pe124(L))[k][1])

def solveHackerRank():
    T = int(input())
    while T:
        T -= 1
        N = int(input())
        print(solve(N))


solveProjectEuler()
#solveHackerRank()
