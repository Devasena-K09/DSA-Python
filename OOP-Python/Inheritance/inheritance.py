class Animal:

    def speak(self):
        print("Animal Sound")


class Dog(Animal):

    def bark(self):
        print("Woof")


dog = Dog()

dog.speak()
dog.bark()
