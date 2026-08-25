# Write a python program to take marks of 3 subjects out of 100. Print True if the studnet scored at least 40 in all three subjects and
# avg marks are at 50.

marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))
print(marks1 >= 40 and marks2 >= 40 and marks3 >=
      40 and (marks1+marks2+marks3)/3 >= 50)
