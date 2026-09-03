# Take a password and check length, presence of @, and whether first and last characters are different.
password=input("Enter password: ")
print("Length of password: ", len(password))
print("Presence of @ at index: ", password.find('@'))
print("First and Last character are different: ", password[0]!=password[-1])