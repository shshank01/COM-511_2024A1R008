# Write a program to input two list and create a third list containg common elements of both the list.
n=list(map(int,input("Enter numbers: ").split()))
m=list(map(int,input("Enter numbers: ").split()))
c=list()
for i in n:
    if i in m:
        c.append(i)
print("List containing common elements: ", c)