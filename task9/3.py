# Write a python program to input marks of 5 students.
# For each student, the program should check whether the entered marks are valid or invalid. 
# Marks are considered valid only if they are between 0 and 100. If the marks are invalid, the program
# should display "Invalid marks skipped" and move to the next student without printing those marks.
# If the marks are valid, the program should display the marks as valid.
ls=[]
ls=list(map(int,input("Enter the marks of 5 students: ").split()))
for i in ls:
    if i<0 or i>100:
        print("Invalid marks skipped.")
    else:
        print("Valid marks:", i)