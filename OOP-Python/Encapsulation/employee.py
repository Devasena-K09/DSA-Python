class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):

        if salary > 0:
            self.__salary = salary


employee = Employee("John", 50000)

employee.set_salary(60000)

print(employee.get_salary())
