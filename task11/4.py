# Write a program to print an inverted right angled triangle using stars.
# ****
# ***
# **
# *
for i in range(4):
    for j in range(4-i):
        print("*", end=" ")
    print()