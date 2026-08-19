class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


student = Student("Devasena", 22)

student.display()
