"""
A short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""

def odd_squares(n):
    squares = [i**2 for i in range(1, n, 2)]

    return sum(squares)

print(odd_squares(5))

a = []
count = 1
b = 1
while count <= 9:
    a.append(b)
    b = b * 2
    count += 1
print(a)