#!/usr/local/bin/python3

#Solution to https://projecteuler.net/problem=55


def isPalin(n):
    return str(n) == str(n)[::-1]

def reverse(n):
    return int(str(n)[::-1])

def lychrel(n, iter):
    if iter > 50: return True
    next = n + reverse(n)
    if isPalin(next): return False
    return lychrel(next, iter+1)

def solve(n):
    return lychrel(n,0)

print len(filter(solve, range(1,10001)))
    
