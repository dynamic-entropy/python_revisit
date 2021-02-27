
# Class variable

class Employee:

    raise_amt = 1.10
    employee_count = 0

    def __init__(self, first, last, pay, department):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.department = department
        self.email = f'{self.firstname}.{self.lastname}@school.com'

        Employee.employee_count += 1

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)


if __name__ == "__main__":

    print("Initial Employee Count: ", Employee.employee_count)
    emp1 = Employee("Rahul", "Chauhan", 100, "itsm")
    emp2 = Employee("Alice", "Singh", 100, "csm")
    print("Final Employee Count: ", Employee.employee_count)

    print("Employee pay before raise: ", emp1.pay, emp2.pay)
    emp1.apply_raise()
    emp2.apply_raise()
    print("Employee pay after raise: ", emp1.pay, emp2.pay)

    Employee.raise_amt = 2
    print("Raise amounts after class variable increment: ",
          emp1.raise_amt, emp2.raise_amt, Employee.raise_amt)

    emp1.raise_amt = 1.5
    print("Raise amounts after instance variable increment: ",
          emp1.raise_amt, emp2.raise_amt, Employee.raise_amt)

    emp1.apply_raise()
    emp2.apply_raise()
    print("Employee pay with different raise_amt: ", emp1.pay, emp2.pay)
