# Write a python program to tak etwo inputs a and b, swap their values using temp variable an dprint the updated values.
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
temp=a
a=b
b=temp
print("Updated value of a: ", a)
print("Updated value of b: ", b)