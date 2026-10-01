'''
Write a python program to convert temperature to and from Celsius to Fahrenheit without functions.
'''

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)