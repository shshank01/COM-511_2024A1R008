# Write a python program to create a simple password validation system
# The program should repeatedly ask the user to enter the password until a valid password is entered.
# A password will be considered valid only if it has at least 8 characters and contain the @ symbol.

while 1:
    password=input("Enter the password: ")
    if '@' in password and len(password)>=8:
        print("Password is valid.")
        break
    else:
        print("Password is invalid. Please try again.")