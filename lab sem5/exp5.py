# Write a program to perform searching activity using linear and binary search.
ls=list(map(int,input("Enter the list: ").split()))
n=int(input("Enter the number to be searched: "))
# Linear search
for i in range(len(ls)):
    if ls[i]==n:
        print("Element found at index",i)
        break
else:
    print("Element not found")
# binary search
ls1=list(map(int,input("Enter the list: ").split()))
n1=int(input("Enter the number to be searched: "))
ls1.sort()
low=0
high=len(ls)-1
while low<=high:
    mid=(low+high)//2
    if ls[mid]==n:
        print("Element found at index",mid)
        break
    elif ls[mid]<n:
        low=mid+1
    else:
        high=mid-1
