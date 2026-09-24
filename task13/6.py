# Write a python program to store one student data as a tuple: name, roll number, and marks. Display grade based on marks.
name=input("Entre name: ")
roll=int(input("Enter roll number: "))
marks=int(input("Enter marks: "))
student=(name, roll, marks)
if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
elif marks>=60:
    print("Grade: D")
else:
    print("Grade: F")