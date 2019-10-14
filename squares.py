squares = []
for value in range(1, 11):
    square = value**2
    multiple = square * 2
    squares.append(multiple)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares = [(value**2)*2 for value in range(1, 11)]
print(squares)