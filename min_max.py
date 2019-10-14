"""
A Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""

def minmax(data):
    smallest_numb = data[0]
    largest_numb = 0
    for number in data:
        if number <= smallest_numb:
            smallest_numb = number
        if number >= largest_numb:
            largest_numb = number
    return smallest_numb, largest_numb

print(minmax([5, 64, 99032, 321, 54, 1, 37]))
