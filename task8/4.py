# Take name,branch, and year. Generate a code name using string concatenation, slicing and repetition.
name=input("Enter name: ")
branch=input("Enter branch name: ")
year=input("Enter year: ")
code_name=name[0:3]*2+branch[0:2]*3+year[-1]
print("Code name: ", code_name)