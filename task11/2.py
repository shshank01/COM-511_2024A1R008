# Write a program to print a square pattern of starts for n rows and n columns.
# * * * *
# * * * *
# * * * *
# * * * *
r=int(input("Entre the number of rows:"))
c=int(input("Enter the number of columns: "))
for i in range(r):
    for j in range(c):
        print("*", end =" ")
    print()