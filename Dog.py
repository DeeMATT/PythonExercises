class Dog:

    def __init__(self, name, day, month, year, sound):
        self.name = name
        self.day = day
        self.month = month
        self.year = year
        self.sound = sound

    def getName(self):
        return self.name

    def birthDate(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)

    def speak(self):
        return self.sound

    def changeBark(self, new_sound):
        self.sound = new_sound

    def __add__(self, otherDog):
        return Dog("Puppy of " + self.name + " and " + otherDog.name, \
                   self.month, self.day, self.year + 1, \
                   self.sound + otherDog.sound)

def main():
    boyDog = Dog("Mesa", 5, 15, 2004, "WOOOF")
    girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
    print(boyDog.speak())
    print(girlDog.speak())
    print(boyDog.birthDate())
    print(girlDog.birthDate())
    boyDog.changeBark("woofywoofy")
    print(boyDog.speak())
    print(boyDog.speak())
    puppy = boyDog + girlDog
    print(puppy.speak())
    print(puppy.getName())
    print(puppy.birthDate())

if __name__ == "__main__":
    main()
