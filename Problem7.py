#!/usr/local/bin/python3

# https://projecteuler.net/problem=7
# https://www.hackerrank.com/contests/projecteuler/challenges/euler007

# Brute force

import math

def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True #2 and 3 are prime
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True #we have already excluded 4,6 and 8.
    elif n % 3 == 0:
        return False
    else:
        r=math.ceil( math.sqrt(n) ) # n rounded to the greatest integer r so that r*r<=n
        f=5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f=f+6
    return True


T = int(input())
primes = list([2,3,5])
while T:
    T -= 1
    N = int(input())

    cnt = 1
    i = 3
    last = primes[len(primes)-1] + 2
    while len(primes) < N:
        if is_prime(last):
            primes.append(last)
        last += 2

    print(primes[N-1])

