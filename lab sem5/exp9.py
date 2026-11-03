class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, emp_id, name, salary, language):
        super().__init__(emp_id, name, salary)
        self.language = language

    def display(self):
        super().display()
        print("Language:", self.language)


m1 = Manager(101, "Rahul", 50000, "HR")
d1 = Developer(102, "Aman", 40000, "Python")

print("Manager Details:")
m1.display()

print("\nDeveloper Details:")
d1.display()