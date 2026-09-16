# Write a python program to input marks of n students in a list. Display the highest marks, lowest marks, average marks, 
# and number of student who passed.
marks=list(map(int,input("Enter the marks of students: ").split()))
print("Highest marks: ", max(marks))
print("Lowest marks: ", min(marks))
print("Average marks: ", sum(marks)/len(marks))
c=0
for i in marks: 
    if i>=30:
        c+=1
print("Number of student passed: ", c)