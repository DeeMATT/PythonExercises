def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('deematt', 'python', 'eggs', 'test')

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} : {1}".format(key, value))

greet_me(client1="Damilola", client2="Samuel")

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

arg = ("two", 3, 5)
kwgs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(*arg)
print("\n")
test_args_kwargs(**kwgs)


def func(age, *args, **kwargs):
    print("This is my first positional argument")
    print("I will marry at the age of " + str(age) + ".")

    print("The following is a set of my unkeyworded arguments")
    for arg in args:
        print(arg)
    print("The following are my keyworded arguments")
    for k, v in kwargs.items():
        print(k, ":", v)

food = ('yam', 'beans', 'rice', 'oil')
details = {'name':'Damilola', 'ag':30, 'address':'#5, Lord Oyewo Drive'}
func(30, food, details)
