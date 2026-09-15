# Write a program to print a square pattern of starts for n rows and n columns.
# * * * *
# * * * *
# * * * *
# * * * *
n=int(input("Enter the number of rows and column:"))
for i in range(n):
    for j in range(n):
        print("*", end =" ")
    print()