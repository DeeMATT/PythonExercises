def manipulate_generator(generator, n):

        c = generator
        b = next(c)
        print(b )

def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1
ma

k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    print(manipulate_generator(g, n))