'''Write a python program to take input from the user without typecasting and multiply it by 3.
Then typecast the same input to int and multiply it by 3. Print both results to show the difference'''

n1 = input("Enter a number: ")
print("Without typecasting: ", n1*3)
n2 = int(n1)
print("With typecasting: ", n2*3)
