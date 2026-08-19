class Employee:

    def __init__(self, emp_id, name, salary):

        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):

        print(
            f"ID: {self.emp_id}"
        )

        print(
            f"Name: {self.name}"
        )

        print(
            f"Salary: ₹{self.salary}"
        )


employees = [

    Employee(
        101,
        "Devasena",
        50000
    ),

    Employee(
        102,
        "Alex",
        60000
    )
]

for employee in employees:

    employee.display()

    print("-" * 20)
