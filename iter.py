data = [1, 2, 3, 4, 5]

i = iter(data)
while i:
    try:
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))
    except StopIteration:
        print('end of iteration')