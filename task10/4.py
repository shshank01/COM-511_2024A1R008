# Write a python program to check whether a number is perfect number. 
# A number is perfect if the sum of its proper divisors is equal to the number itself.
n=int(input("Enter the number: "))
add=0
for i in range(1,n//2+1):
    if n%i==0:
        add+=i
if add==n:
    print(f"{n} is perfect number")
else:
    print(f"{n} is not perfect number")