# write a python program to take an amount in rupee and calculate how many 500 and 100 notes are needed
a = int(input("Enter the amount: "))
print("500 notes: ", a//500)
print("100 notes: ", (a%500)//100)