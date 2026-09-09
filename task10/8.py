# Write a python program to repeatedly calculat ethe sum of digits of a number until the result become single digit.
n=int(input("Enter the number: "))
while n>=10:
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    n=sum
print(n)