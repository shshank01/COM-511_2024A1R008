# Write a python program to input two numbers and find their greatest common divisor using a loop.

a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
while b!=0:
    a,b=b,a%b
print("GCD of two numbers are: ", a)