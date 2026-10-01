'''
6. Write a program to reverse every k-th row in a matrix
'''

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

k = int(input("Enter k: "))

for i in range(rows):
    if (i + 1) % k == 0:
        matrix[i] = matrix[i][::-1]

print("Matrix after reversing every k-th row:")
for row in matrix:
    print(row)