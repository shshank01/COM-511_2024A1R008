'''Create an Electricity Bill class that stores a customer's name and electricity units used. Calculate the bill using these rates:
rs 3 per unit for the first 100 units
rs 5 per unit for the next 100 units
rs 7 per unit for the units above 200.
Display the customer's name, units used, and total bill amount.
If the entered units are negative, display an error message.'''

class ElectricityBill:
    def __init__(self,name,units,bill):
        self.name=name
        self.units=units
        self.bill=bill
    def calculate_bill(self):
        if self.units<0:
            print("Error: Units cannot be negative.")
        else:
            if self.units<=100:
                self.bill=self.units*3
            elif self.units<=200:
                self.bill=100*3+(self.units-100)*5
            else:
                self.bill=100*3+100*5+(self.units-200)*7
    def display(self):
        print("Customer Name:",self.name)
        print("Units Used:",self.units)
        print("Total Bill Amount:",self.bill)
name=input("Enter the customer's name: ")
units=int(input("Enter the electricity units used: "))
bill=ElectricityBill(name,units,0)
bill.calculate_bill()
bill.display()