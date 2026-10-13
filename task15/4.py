'''BankAccount class
Create a BankAccount class that stores an account holder's name and balance. 
Add instance methods to deposit money, withdraw money, and display the balance. 
Do not allow a withdrawal greater than the available balance.'''


class BankAccount:
    def __init__(self, name, bal):
        self.name = name
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt

    def withdraw(self, amt):
        if amt > self.bal:
            print("Insufficient balance")
        else:
            self.bal -= amt

    def display(self):
        print("Account holder name:", self.name)
        print("Balance:", self.bal)


name = input("Enter account holder name: ")
bal = float(input("Enter the initial balance: "))
dep = float(input("Enter the amount to deposit: "))
withdraw = float(input("Enter the amount to withdraw: "))
account = BankAccount(name, bal)
account.deposit(dep)
account.withdraw(withdraw)
account.display()
