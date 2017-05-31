#!/bin/python3

'''

https://projecteuler.net/problem=26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

'''


from datetime import date
import math

def esieve(n):
    '''Returns a list of all primes less than N'''

    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

P = sorted(esieve(10000), reverse=True)

def get_reciprocal_cycles_length(N):
    if N < 8: return 3
    for d in P:
        if d < N:
            period = 1
            while pow(10, period, d) != 1: period += 1
            if d-1 == period:
                break
    return d

def calculate_reciprocal_cycles_length(N):
    DP = []
    if N < 8: return 3
    for d in P:
        period = 1
        while pow(10, period, d) != 1: period += 1
        if d-1 == period:
            DP.append(d)
    return DP

def solve_project_euler():
    print(get_reciprocal_cycles_length(10000))

# solve_project_euler()

def solve_hacker_rank():

    # DP = calculate_reciprocal_cycles_length(10000)
    # DP = sorted(DP, reverse=True)
    T = int(input().strip())
    while T:
        T -= 1
        N = int(input().strip())
        print(get_reciprocal_cycles_length(N))

solve_hacker_rank()