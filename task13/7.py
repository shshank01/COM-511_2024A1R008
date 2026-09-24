# Write a python program to store multiple student records as a list of tuples. 
# Each tuple should contain name,roll number, and marks. Display students who scored above 75.
ls=[('aditya',1,78),('reena',2,89),('meena',3,56),('samay',4,90),('parth',5,21)]
for i in ls:
    if i[2]>75:
        print(i)