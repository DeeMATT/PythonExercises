"""
A short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def squares(n):
    squares = [i**2 for i in range(n)]
    return sum(squares)

print(squares(5))