# Write a program to print the following pattern for n rows
# 1
# 1 2
# 1 2 3
# 1 2 3 4
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()