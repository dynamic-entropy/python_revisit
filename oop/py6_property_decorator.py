class Employee:

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay

    def __str__(self):
        return f'{self.fullname} - {self.email}'

    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@school.com'

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.firstname = first
        self.lastname = last

    @fullname.deleter
    def fullname(self):
        self.firstname = None
        self.lastname = None


if __name__ == "__main__":

    emp1 = Employee("Rahul", "Chauhan", 35000)
    emp2 = Employee("Alice", "Singh", 43000)
    print(emp2)
    emp2.fullname = "Bob Kumar"
    print(emp2)

    del emp1.fullname
    print(emp2)
    print(emp1)
