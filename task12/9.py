# Write a python program to count how many times a particular element appears in a list
n=list(map(int,input("Enter numbers: ").split()))
a=int(input("Enter a number: "))
c=0
for i in n:
    if i==a:
        c+=1
print("Number of times", a, "appears in list: ", c)