"""
A Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

def even(k):

    if type(k) is int:                  # check if the value of argument is integer
        convert = str(k)
        even_keys = ['0', '2', '4', '6', '8']       # five numbers that every even number ends with

        # check if the last digit of the converted argument exists among even_keys
        if convert[-1] in even_keys:
            return True
        else:
            return False
    else:
        return "TypeError: even() takes only integers"

print(even(34256785687))
