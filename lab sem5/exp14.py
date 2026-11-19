''' Create a text file “MyFile1.txt” in python and ask the user to write separate 3 lines with three input 
statements from the user. '''

f = open("MyFile.txt", "w")

line1 = input("Enter first line: ")
line2 = input("Enter second line: ")
line3 = input("Enter third line: ")

f.write(line1 + "\n")
f.write(line2 + "\n")
f.write(line3 + "\n")

f.close()

print("File created successfully.")