def greet_user(username, location, age=25):
    """Display a simple greeting."""
    print("Hello, " + username)
    print("You are " + str(age) + " years old")
    print("You live in " + location)

greet_user("Bola", location="Ikeja", age=30)
