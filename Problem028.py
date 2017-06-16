#!/bin/python3

'''

https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

'''


from datetime import date
import math
from math import sqrt


def G(n):
    s = int((n - 1) / 2)
    return int((16 * s * s * s + 30 * s * s + 26 * s + 3) / 3)

def solve_project_euler():
    print(G(1001))

solve_project_euler()

def solve_hacker_rank():
    T = int(input().strip())
    while T:
        T -= 1
        N = int(input().strip())
        if N == 1:
            print(1)
        else:
            print(G(N))

# solve_hacker_rank()