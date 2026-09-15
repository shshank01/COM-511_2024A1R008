# Write a python program to print Floyd's triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
n=1
for i in range(4):
    for j in range(i+1):
        print(n, end=" ")
        n+=1
    print()