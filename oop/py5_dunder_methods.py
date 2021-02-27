
class Employee:

    raise_amt = 1.10
    employee_count = 0

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.email = f'{self.firstname}.{self.lastname}@school.com'

        Employee.employee_count += 1

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        pay = int(pay)
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return f'Employee({self.firstname},{self.lastname},{self.pay})'

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


if __name__ == "__main__":
    emp1 = Employee("Rahul", "Chauhan", 10000)
    print(emp1)

    emp2 = Employee("Alice", "Sharma", 20000)
    print(emp1+emp2)

    print(len(emp1))
