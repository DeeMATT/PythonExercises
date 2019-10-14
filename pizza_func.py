def make_pizza(*toppings):
    """print the list of toppings that have been requested."""
    for topping in toppings:
        print(topping)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')