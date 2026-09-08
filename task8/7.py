# Write a python program to simulate a digital lock system.
# The lock should ask the user to enter a 4-digit PIN. If the entered PIN does not contain exactly 4 digits, 
# the program should display an error message and ask again. If the entered PIN is correct,
# the lock should open. Otherwise, the program should ask the user to try again.
PIN='1234'
pin=input("Enter a 4-digit PIN: ")
if len(pin)!=4:
    print("Error: PIN must be exactly 4 digits.")
    pin=input("Enter a 4-digit PIN: ")
if pin==PIN and len(pin)==4:
    print("PIN accepted. Lock opened.")
else:
    print("Incorrect PIN. Please try again.")
