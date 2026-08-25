# Write a python program to swap two numbers without using a third variable
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
a=a+b
b=a-b
a=a-b
print("Updated value of a: ",a)
print("Updated value of b: ",b)
