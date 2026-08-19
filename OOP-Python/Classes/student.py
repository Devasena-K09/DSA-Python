class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Branch: {self.branch}")


student1 = Student(
    "Devasena",
    22,
    "Electrical & Electronics Engineering"
)

student1.display()
