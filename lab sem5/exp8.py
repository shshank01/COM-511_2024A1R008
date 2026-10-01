'''
8. Create a database using lists and tuples. Each student record must contain roll number, name, branch and CGPA.
Store each record as a tuple inside a list. Display all records and search for a student using roll number.
Condition:
    1. Each record should be stored as a tuple
    2. The complete database should be stored as a list
    3. Roll numbers must be unique.
'''

student_records = []

while True:
    roll = int(input("Enter roll number: "))
    while (any(record[0] == roll for record in student_records)):
        roll = int(input("Roll number already exists. Enter another roll number: "))
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))

    student_record = (roll, name, branch, cgpa)
    student_records.append(student_record)

    choice = input("Do you want to add more records? (yes/no): ")
    if choice.lower() != "yes":
        break

print("\nStudent Records:")
print("Name\tRoll\tBranch\tCGPA")
for record in student_records:
    print(f"{record[1]}\t{record[0]}\t{record[2]}\t{record[3]}")

search_roll = int(input("\nEnter roll number to search: "))
for record in student_records:
    if record[0] == search_roll:
        print(f"Name: {record[1]}, Roll: {record[0]}, Branch: {record[2]}, CGPA: {record[3]}")
        break
else:
    print("Record not found.")