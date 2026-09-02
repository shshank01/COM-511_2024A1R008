# Write a python program to take a password and check whether it contains @ and has at least 8 characters.
password=input("Enter the password: ")
print(password.find('@'))
print(len(password)>=8)
