#Implementing map in lambda

items = list(range(6))
squared = list(map(lambda x: x**2, items))
print(squared)

#Implementing Filter in lambda

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)


