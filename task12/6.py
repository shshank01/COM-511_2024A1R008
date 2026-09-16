# Write a python program to input numbers in a list and create two separate lists for even and odd numbers.
n=list(map(int,input("Enter numbers: ").split()))
even=list()
odd=list()
for i in n:
    if i%2==0 and i!=0:
        even.append(i)
    elif i!=0:
        odd.append(i)
print("List containing even numbers: ", even)
print("List containing odd numbers: ", odd)