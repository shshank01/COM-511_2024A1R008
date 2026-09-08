# Write a python program to determine whether a student is eligible for a scholarship
# The scholarship should be granted if the student satisfies either of the following conditions:
# 1. The student has a CGPA of 8.5 or above and attendance of 85 percent or above.
# 2. The student has won a national-level competition.
# The program should take CGPA, attendance percentage, and national-level competition status as input, 
# then display whether the student is eligible for the scholarship.
cgpa=input("Enter your CGPA: ")
attendance=input("Enter your attendance percentage: ")
comp_status=input("Have you won a national-level competition? (yes/no): ")
if float(cgpa)>=8.5 and float(attendance)>=85 or comp_status.lower()=="yes":
    print("You are eligible for the scholarship.")
else:
    print("You are not eligible for the scholarship.")