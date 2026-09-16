# Write a python program to input marks of 10 students. Store only valid marks between 0 and 100 in a list. Skip invalid marks.
marks=list(map(int,input("Enter marks of students: ").split()))
for i in marks:
    if i<0 or i>100:
        marks.remove(i)
print("Updated list: ", marks)