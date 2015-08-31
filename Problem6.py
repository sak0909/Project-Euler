#!/usr/local/bin/python3

# https://projecteuler.net/problem=6
# https://www.hackerrank.com/contests/projecteuler/challenges/euler006

# Summation of series n: n(n+1)/2
# Summation of squares formula: n(n+1)(2n+1)/6


T = int(input())
while T:
    T -= 1
    N = int(input())
    square_of_summation_series = (N*(N+1))/2
    square_of_summation_series *= square_of_summation_series

    summation_of_square_series = (N*(N+1)*((2*N)+1))/6

    print(int(square_of_summation_series - summation_of_square_series))

