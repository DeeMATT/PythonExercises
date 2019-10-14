cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    if car == 'bmw' or car == 'toyota':
        print(car.upper())
    else:
        print(car.title())