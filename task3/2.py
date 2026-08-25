# Write a python program to take a 2-digit number as input and print the sum of its digit
n=int(input("Enter 2-digit number: "))
s=0
temp=n
while temp!=0:
    s+=temp%10
    temp=temp//10
print("Sum of the digits are: ", s)