'''
Write a program to demonstrate type checking of various data types and demonstrate the use of 
following built in functions in python: abs(), len(), min(), round(), isalnum(), type().
'''

# Type checking of various data types

a = 10
b = 3.14
c = "Hello"

print("Type(10):", type(a))
print("Type(3.14):", type(b))
print("Type('Hello'):", type(c))

# Demonstrating built-in functions
# abs() function
num = -5
print("abs(-5):", abs(num))

# len() function
text = "Hello, World!"
print("len('Hello, World!'):", len(text))

# min() function
numbers = [5, 2, 8, 1, 9]
print("min([5, 2, 8, 1, 9]):", min(numbers))

# round() function
decimal = 3.14159
print("round(3.14159):", round(decimal))

# isalnum() function
s1 = "Hello123"
s2 = "Hello 123"
print("isalnum('Hello123'):", s1.isalnum())
print("isalnum('Hello 123'):", s2.isalnum())
