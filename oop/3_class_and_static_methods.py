# Class and Static Methods


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


if __name__ == "__main__":

    employee1 = "Rahul-Chauhan-100"
    emp1 = Employee.from_string(employee1)
    print(emp1.fullname())

    import datetime
    new_date = datetime.date.today()
    print(Employee.is_workday(new_date))
