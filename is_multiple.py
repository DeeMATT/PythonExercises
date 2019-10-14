"""
A python function that takes two integer values
and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""
def is_multiple(n, m):

    # If n is a multiple of m, it should be completely divisible by m without any remainders
    if (n % m) == 0:        # Conditional test to check is_multiple
        return True
    else:
        return False

# A call on the defined function to determine if n is multiple of m
print(is_multiple(19, 3))