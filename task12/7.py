# Write a python program to rotate a list one position to the right
n=list(map(int,input("Enter numbers: ").split()))
last=n.pop()
n.insert(0, last)
print("Rotated list: ", n)
