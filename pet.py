def describe_pet(pet_name, age, health, animal_type='dog', location='Nigeria'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + " that is " + health + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    print(pet_name.title() + " is " + str(age) + " years old and located in " + location + ".")


describe_pet('hamster', 10, 'sick', 'lamb', 'ghana')