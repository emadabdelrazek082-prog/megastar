# MegaStar Employee Management System

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def get_subordinates(self):
        return self.subordinates

    def __str__(self):
        return f'{self.name} - {self.position}'

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 'Manager')

class Developer(Employee):
    def __init__(self, name):
        super().__init__(name, 'Developer')

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees

# Example Usage
if __name__ == '__main__':
    company = Company()
    manager = Manager('Alice')
    developer1 = Developer('Bob')
    developer2 = Developer('Charlie')

    company.add_employee(manager)
    company.add_employee(developer1)
    company.add_employee(developer2)

    manager.add_subordinate(developer1)
    manager.add_subordinate(developer2)

    for employee in company.get_employees():
        print(employee)
        if isinstance(employee, Manager):
            print('Subordinates:')
            for sub in employee.get_subordinates():
                print(f'- {sub}')