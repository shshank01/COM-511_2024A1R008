# Write a python program to input numbers in a list and find the second largest number.
marks=list(map(int,input("Enter marks of students: ").split()))
max=float("-inf")
smax=float("-inf")
for i in marks:
    if i>max:
        smax=max
        max=i
    elif smax<i<max:
        smax=i
print("Second largets number in list: ", smax)