def fibon(n):
    result = []
    a = b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

for x in fibon(1000):
    print(x)