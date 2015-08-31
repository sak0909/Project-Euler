#!/usr/local/bin/python3
#Solution to problem 81: Path sum: two ways
#Recursive algorithm using memoization


import math
import sys

f = open('p081_matrix.txt')
input = []

for i in f:
  row = i[:-1]
  row = row.split(',')
  row = map(int, row)
  input.append(row)
f.close()

#print(input[1])
#print(len(input[0]))
#print(len(input[0]))
ans = [[0 for col in range(len(input))] for row in range(len(input))]

def MinPath(input, i, j):
  if i >= len(input):
    return sys.maxint
  if j >= len(input[i]):
    return sys.maxint
  if (i == len(input)-1) and (j == len(input)-1):
    ans[i][j] = input[i][j]
    return input[i][j]
  if ans[i][j] == 0:
    val = min( MinPath(input, i+1, j), MinPath(input, i, j+1) )
    ans[i][j] = input[i][j] + val
    #print("Returning " + str(input[i][j]) + "+" + str(val) + " for i,j: " + str(i) + " " + str(j))
  return ans[i][j]

print(MinPath(input, 0, 0))
