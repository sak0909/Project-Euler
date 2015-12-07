#!/usr/local/bin/python3

# https://projecteuler.net/problem=20
# https://www.hackerrank.com/contests/projecteuler/challenges/euler020

# Bruteforce


def factorial(n):
    assert n >= 0
    result = 1
    for i in range(1, n + 1):
        result = (result * i)
    return result


def solve(n):
    f = str(factorial(n))
    ans = sum([int(i) for i in f])
    return ans


def solveHackerRank():
    T = int(input())
    while T:
        T -= 1
        n = int(input())
        print(solve(n))


def solveProjectEuler():
    print(solve(100))


#solveProjectEuler()
solveHackerRank()



