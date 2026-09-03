# Take roll number like 2024A1R057 and extract admission year, program code, and roll number digit using slicing.
roll=input("Enter roll number: ")
yr=roll[0:4]
prgm_code=roll[4:6]
roll_no=roll[7:]
print("Admission year: ", yr)
print("Program code: ", prgm_code)
print("Roll number: ", roll_no)