'''
7. Write a Python program to create records of n students. Store each student record as a dictionary
containing roll number, name, branch, and marks. Store all records in a list and search for a student using
roll number (Condition: Roll number must be unique).
'''

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    roll = int(input("Enter roll number: "))

    while any(student["roll"] == roll for student in students):
        print("Roll number already exists.")
        roll = int(input("Enter roll number: "))

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

search_roll = int(input("\nEnter roll number to search: "))
for student in students:
    if student["roll"] == search_roll:
        print("\nStudent found:")
        for k, v in student.items():
            print(f"{k}: {v}")
        found = True
        break
else:
    print("Student not found")