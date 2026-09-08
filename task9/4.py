# Write a python program to input four numbers from the user and find the greatest number among them.
ls=[]
ls=list(map(int,input("Enter four numbers: ").split()))
print("Greatest number is: ",max(ls))