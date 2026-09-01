'''Write a python program to take a student name and roll number, 
then generate a username using the first 3 letters of the name and last 2 digit of the roll number.'''
name = input("Enter your name: ")
rollno = input("Enter your roll number: ")
username = name[:3]+rollno[-2:]
print(username)
