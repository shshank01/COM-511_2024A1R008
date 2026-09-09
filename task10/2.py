# Write a python program to input a number and check whether it is prime
n=int(input("Enter a number: "))
for i in range(2, n//2):
    if n%i==0 or n==0 or n==1 :
        print(f"{n} is not prime")
        break
else:
    print(f"{n} is prime")