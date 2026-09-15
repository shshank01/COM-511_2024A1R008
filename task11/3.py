# Write a program to print a right angled triangle using stars.
# *
# **
# ***
# ****
for i in range(4):
    for j in range(i+1):
        print("*", end=" ")
    print()