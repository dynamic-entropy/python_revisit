from py3_class_and_static_methods import Employee


class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        self.employees.append(emp)

    def remove_employee(self, emp):
        self.employees.remove(emp)

    def print_employees(self):
        print("")
        for emp in self.employees:
            print("-->", emp.fullname(), end=" ")


if __name__ == "__main__":

    dev1 = Developer("Rahul", "Chauhan", 50000, "Python")
    dev2 = Developer("Alice", "Sharma", 60000, "Javascript")

    manager1 = Manager("Bob", "Singh", 70000, [dev1])

    print(manager1.fullname(), manager1.email)

    manager1.print_employees()
    manager1.add_employee(dev2)
    manager1.print_employees()
    manager1.remove_employee(dev1)
    manager1.print_employees()
