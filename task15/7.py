'''Create an Employee class that stores an employee's name, basic salary, house rent allowance (HRA) percentage,
travel allowance and deductions. Add instance methods to calculate the gross salary and net salary.
Gross salary is the basic salary plus HRA and travel allowance. Net salary is the gross salary minus deductions.
Display the employee's name, gross salary and net salary.'''

class Employee:
    def __init__(self,name,bsal,hra,ta,ded):
        self.name=name
        self.bsal=bsal
        self.hra=hra
        self.ta=ta
        self.ded=ded
    def gross_salary(self):
        return self.bsal+(self.bsal*self.hra/100)+self.ta
    def net_salary(self):
        return self.gross_salary()-self.ded
name=input("Enter employee's name: ")
bsal=float(input("Enter basic salary: "))
hra=float(input("Enter house rent allowance (HRA): "))
ta=float(input("Enter travel allowance: "))
ded=float(input("Enter deductions: "))
emp=Employee(name,bsal,hra,ta,ded)
print("Employee Name:",emp.name)
print("Gross Salary:",emp.gross_salary())
print("Net Salary:",emp.net_salary())