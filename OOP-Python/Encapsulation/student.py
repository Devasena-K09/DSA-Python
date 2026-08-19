class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):

        if 0 <= marks <= 100:
            self.__marks = marks


student = Student("Alice", 85)

student.set_marks(95)

print(student.get_marks())
