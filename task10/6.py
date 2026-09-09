# Write a python program to input a decimal number and convert it into binary without using the built-in bin() function.
n=int(input("Enter a number: "))
s=""
while n!=0:
    temp=n%2
    s+=str(temp)
    n=n//2
print(s[::-1])