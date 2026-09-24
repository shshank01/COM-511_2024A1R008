# Write a python program to show that tuple values cannot be changed directly. 
# Convert tuple into list, update it, and convert it back into tuple.
tup=('a', 'b', 'c', 'd', 'e')
lst=list(tup)
lst[0]='A'
tup=tuple(lst)
print(tup)
