# Take student full name and roll number. Generate email using first 3 letters of first name, first 3 letters of last name, and last 3 characters of roll number.
name=input("Enter full name: ")
roll=input("Enter roll number: ")
index=name.find(" ")
last=name[index+1:]
email=name[0:3]+last[0:3]+roll[-3:]+"@gmail.com"
print(email)