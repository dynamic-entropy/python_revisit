
#Classes and Instances

class Employee:

    def __init__(self, first, last, pay, department):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.department = department
        self.email = f'{self.firstname}.{self.lastname}@school.com'

    def fullname(self):
        return f'{self.firstname} {self.lastname}'


if __name__ == "__main__":

    emp1 = Employee("Rahul", "Chauhan", 350.7, "itsm")
    emp2 = Employee("Alice", "Singh", 430.4, "csm")

    print(emp1)
    print(emp2)

    print(Employee.fullname(emp1))
    print(emp2.fullname())
