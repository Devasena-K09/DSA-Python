class Employee:

    def company(self):
        print("Works at XYZ Company")


class Developer(Employee):

    def code(self):
        print("Writing code")


class Tester(Employee):

    def test(self):
        print("Testing software")


developer = Developer()
tester = Tester()

developer.company()
developer.code()

tester.company()
tester.test()
