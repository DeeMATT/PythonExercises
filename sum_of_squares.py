"""
A short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def sum_of_squares(numb):

    numbers = range(numb)
    squares = [number**2 for number in numbers]
    print(squares)
    return sum(squares)

print(sum_of_squares(67))