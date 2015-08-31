#!/usr/local/bin/python3

# https://projecteuler.net/problem=2
# https://www.hackerrank.com/contests/projecteuler/challenges/euler002

# Brute force and cache lookup

import collections
def fillFibCache():
    a,b=1,2
    S=0
    N=4*pow(10,16)
    cache =  collections.OrderedDict()
    while b<=(N):
        if (b%2 == 0):
            S+=b
            cache[b]=S
        a,b=b,a+b
    return cache

c=fillFibCache()

T=int(input())
while(T > 0):
    T-=1
    N=int(input())
    candidate = 2
    for key in c:
        if key>N:
            break
        candidate=key
    print(c[candidate])
