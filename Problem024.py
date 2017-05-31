#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    results = [i+(5-(i%5)) if (i >= 38 and 5-(i%5) < 3) else i for i in grades]
    return results

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
# print(grades, result)
print ("\n".join(map(str, result)))