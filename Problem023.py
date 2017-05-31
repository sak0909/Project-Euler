#!/bin/python3

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown
 that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the
  greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''


from datetime import date
import math

def divisors(n):
    """
    Returns all nontrivial divisors of an integer, but makes no guarantees on the order.
    """
    # "1" is always a divisor (at least for our purposes)
    yield 1

    largest = int(math.sqrt(n))

    # special-case square numbers to avoid yielding the same divisor twice
    if largest * largest == n:
        yield largest
    else:
        largest += 1

    # all other divisors
    for i in range(2, largest):
        if n % i == 0:
            yield i
            yield n / i

def is_abundant(n):
    S = sum(divisors(n))
    return S > n

abundants = set([x for x in range(12, 28123 + 1) if is_abundant(x)])
#print(abundants)

sum_of_twos = set()
for i in abundants:
    for j in abundants:
        sum_of_twos.add(i+j)

print(sum_of_twos)

def solve_project_euler():
    ans = 0
    for i in range(1, 28123+1):
        if i not in sum_of_twos:
            ans += i
    print (ans)

def solve_hacker_rank():

    T = int(input().strip())
    while T:
        T -= 1
        N = int(input().strip())
        found = 0
        for i in abundants:
            if N-i in abundants:
                found = 1
                break
        if found or N > 28123:
            print("YES")
        else:
            print("NO")

# solve_hacker_rank()