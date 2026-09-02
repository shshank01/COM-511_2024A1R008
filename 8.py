# Write a python program to take a string and separate characters present at even index position and odd index position
string=input("Enter a string: ")
odd=string[::2]
even=string[1::2]
print("Odd characters: ", odd)
print("Even characters: ", even)