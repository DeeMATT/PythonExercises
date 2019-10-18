import sys                          # provides getsize function

data = []
for k in range(26):                  # NOTE: must fix choice of n
    a = len(data)                   # number of elements
    b = sys.getsizeof(data)         # actual size in bytes
    print(f'Length: {a}; Size in bytes: {b}')
    data.append(None)               # increase length by one