# Write a python program to input a list of numbers and create a new list containing only unique elements
n=list(map(int,input("Enter numbers: ").split()))
ls=list()
# for i in n:
#     if n.count(i)>=2:
#         n.remove(i)
# print("Updated list: ", n)
# OR
for i in n:
    if n.count(i)>=2:
        n.remove(i)
print("Updated list: ", n)