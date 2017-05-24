#!/usr/local/bin/python3

#Truncatable primes

#https://projecteuler.net/problem=37

#How many different ways can £2 be made using any number of coins?
#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math

from math import sqrt


def esieve(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]



primes = set(esieve(1000000))

def is_prime(n):
    if int(n) in primes:
        return True
    else:
        return False

def is_truncatable(n):
    for d in range(1, len(str(n))):
        if not is_prime(str(n)[d:]) or not is_prime(str(n)[:d]):
            return False
    return True

def solve_project_euler():
    truncatable_numbers = []
    n = 23
    while len(truncatable_numbers) < 11:
        if is_prime(n) and is_truncatable(n):
            truncatable_numbers.append(int(n))
        n += 1

    return truncatable_numbers


truncatable_numbers = solve_project_euler()
# print(sum(truncatable_numbers))
# print(truncatable_numbers)

def solve_hackerrank():
    N = int(input().strip())
    ans = 0
    for i in truncatable_numbers:
        if i < N:
            ans += i

    print(ans)

solve_hackerrank()

