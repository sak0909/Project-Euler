#!/usr/local/bin/python3

# https://projecteuler.net/problem=99
# https://www.hackerrank.com/contests/projecteuler/challenges/euler099

# Use log based comparison

import math
from collections import OrderedDict

def solveProjectEuler():
    biggest = int(0)
    lineNo = int(1)
    biggest_line = int(1)
    f = open('p099_base_exp.txt')
    for line in f:
        numbers = line.split(",")
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        val = math.log(num1) * num2
        if val > biggest:
            biggest = val
            biggest_line = lineNo
        lineNo += 1
    print (biggest)
    print ("\n" + str(biggest_line) )

#solveProjectEuler()

def solveHackerRank():
    N = int(input())
    D = dict()
    for i in range(N):
        numbers = input().split()
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        val = math.log(num1) * num2
        D[val] = (num1, num2)

    K = int(input())
    d_sorted_by_value = OrderedDict(sorted(D.items(), key=lambda x: x[0]))
    ans = list(d_sorted_by_value.items())[K-1][1]
    print(str(ans[0]) + " " + str(ans[1]))

solveHackerRank()
