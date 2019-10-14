def fibonacci():
    a = 0
    b = 1
    while b <= 101:
        yield a
        a, b = b, a+b

for num in enumerate(fibonacci()):
    print(num)