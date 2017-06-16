#!/bin/python3

'''

https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:

n2+n+41n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤390≤n≤39. However, when n=40,402+40+41=40(40+1)+41n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤790≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+bn2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000

where |n||n| is the modulus/absolute value of nn
e.g. |11|=11|11|=11 and |−4|=4|−4|=4
Find the product of the coefficients, aa and bb, for the quadratic expression that produces the maximum number of primes for consecutive values of nn, starting with n=0n=0.

'''


from datetime import date
import math
from math import sqrt

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

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n%2==0 or n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0: return False
        f+= 6
    return True



def solve_project_euler():
    nmax = 0
    p = (0,0)
    for b in esieve(1000):
        for a in range(-b + 2, 0, 2):
            n = 1
            while is_prime(n * n + a * n + b): n += 1
            if n > nmax: nmax, p = n, (a, b)

    print(p, p[0]*p[1])
# solve_project_euler()

def solve_hacker_rank():
    N = int(input().strip())
    nmax = 0
    p = (0,0)
    for b in esieve(N):
        for a in range(-b + 2, 0, 2):
            n = 1
            while is_prime(n * n + a * n + b): n += 1
            if n > nmax: nmax, p = n, (a, b)

    print(p[0], p[1])

solve_hacker_rank()