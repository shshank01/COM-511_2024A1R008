'''
Consider the string “Welcome to Python world”. Perform the following operations: 
Count the number of alphabets in the given string.  
To extract characters in the given, range from the given string.  
Check if the string is alphanumeric or not. 
'''

string = "Welcome to Python world"

# counting the number of alphabets
count = 0
for char in string:
    if char.isalpha():
        count += 1
print("Number of alphabets in the string:", count)

# extracting characters in the given range
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))
extracted_chars = string[start_index:end_index]
print("Extracted characters:", extracted_chars)

# checking if the string is alphanumeric
print("Is the string alphanumeric?", string.isalnum())