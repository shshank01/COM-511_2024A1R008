'''1. Create a class and object: Student details
Problem: Create a Student class to store a student's name and roll number. 
         Create an object and display the details using an instance method.'''


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)


student = Student("Aditya", 1)
student.display()
