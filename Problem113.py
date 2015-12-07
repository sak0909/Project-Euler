#!/usr/local/bin/python3

# https://projecteuler.net/problem=113
# https://www.hackerrank.com/contests/projecteuler/challenges/euler113

# Let n be the number of digits. To count the number of increasing or decreasing numbers using combinatorics,
# let's view each number as a sequence of digit readout slots and operations. For example, suppose n=5 and
# we examine the increasing number 23667. We can express it as the sequence "+ + # + # + + + # # + # + +",
# where # is a digit and + means increment. This way of thinking will be useful, as we will see.
#
# For the set of increasing numbers, each number has n readout slots and 9 increments, positioned arbitrarily.
# Using this construction, the number is guaranteed to be increasing. Note that leading zeros can be produced.
# Conversely, for each increasing number, we can generate a (unique) sequence of slots and increments that represents it
# (putting all unused increments after the rightmost digit). Hence there are n+9 objects to arrange in sequence,
# so there are binomial(n + 9, 9) ways to arrange them. Finally we subtract 1 because 0 can be formed with this scheme,
# which must be excluded from the set of increasing numbers.
#
# For the set of decreasing numbers, each number has n readout slots and 10 operations. Of the 10 operations,
# the leading one must be "increment to 9", and the rest must be decrements. Similar to the increasing case,
# each sequence of slots and decrements produces a decreasing number, and conversely each decreasing number
# corresponds to a unique sequence of slots and decrements. However, 0 can be formed in n+1 ways, by concentrating
# all 10 operations between some pair of slots, e.g. "+9 -9 # # # #", "# +9 -9 # # #", ..., "# # # # +9 -9".
#
# There are 9n repeat numbers, for example: 1, 2, ..., 9; 11, 22, ..., 99; 111, 222, ..., 999; ... (note that 0 is excluded).
# Since they are double-counted in the increasing and decreasing numbers, we subtract the size of this set.
#
# In conclusion, the number of non-bouncy numbers is (binomial(n+9,9) - 1) + (binomial(n+10,10) - (n+1)) - 9n.
#
# (Technically, in the problem statement and this solution, "increasing" actually means "nondecreasing" and "decreasing" means "nonincreasing".)

from math import factorial as fac

n = 100000
k = 10
C = [[0 for x in range(k+1)] for x in range(n+1)]


def preCompute():
    M = 1000000007

    # Calculate value of Binomial Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1

            # Calculate value using previosly stored values
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]

def binomialCoef(n, k):
    M = 1000000007
    return C[n][k]%M

def compute(digits):
    M = 1000000007
    increasing = binomialCoef(digits + 9, 9) - 1
    decreasing = binomialCoef(digits + 10, 10) - (digits + 1)
    flat = digits * 9
    ans = increasing + decreasing - flat
    return ans


def solveHackerRank():
    preCompute()
    T = int(input())
    M = 1000000007
    while T:
        T -= 1
        K = int(input())
        print(compute(K) % M)


def solveProjectEuler():
    print(compute(100))


# solveProjectEuler()
solveHackerRank()



