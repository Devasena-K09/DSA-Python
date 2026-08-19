class Cat:

    def sound(self):
        print("Meow")


class Dog:

    def sound(self):
        print("Woof")


animals = [Cat(), Dog()]

for animal in animals:
    animal.sound()
