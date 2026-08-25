'''Write a python program to take student details like name, roll no, cgpa and hostel status from the user.
Typecast them into appropriate types and print them along with their detected type.'''

name = input("Enter your name: ")
roll_no = int(input("Enter your roll number: "))
cgpa = float(input("Enter your CGPA: "))
hostel_status = bool(input("Enter your hostel status (0/1): "))
print("Name: ", name, " Type: ", type(name))
print("Roll Number: ", roll_no, " Type: ", type(roll_no))
print("CGPA: ", cgpa, " Type: ", type(cgpa))
print("Hostel Status: ", hostel_status, " Type: ", type(hostel_status))
