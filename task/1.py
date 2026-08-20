# write a python program to perform addition, subtraction, multiplication, division of two numbers. also find quotient.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Addition: ", a+b)
print("Subtraction: ", a-b)
print("Multiplication: ", a*b)
print("error" if a==0 else "Division: ", a/b)