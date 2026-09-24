# Write a python program to check whether a given value is present in a tuple. If present, then display its position.
a=(1,2,3,4,5,6,7,8,9,10)
t=int(input("Enter the value to search: "))
if t in a:
    print(f"{t} found at index: ", a.index(t))
else:
    print("Not found")