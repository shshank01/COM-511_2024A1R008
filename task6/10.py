'''Write a python program to take a 10-digit mobile number and display only the last 4 digits. Replace the first 6 digit with ******'''
number=input("Enter 10 digit mobile number: ")
print(number[-4:])
number=number.replace(number[:6],'******')
print(number)