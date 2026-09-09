# Write a python program that asks the user to enter a username and password. The user should get only 3 attempts. 
# If the correct credentials are entered, display "Login Successful" and stop the loop. If all attempts are used,display "Acount Locked"

username="shshank01"
password="shshank@123"
flag=False
for i in range(3):
    user=input("Enter the username: ")
    passw=input("Enter the password: ")
    if user==username and passw==password:
        flag=True
        print("Login Scuccessful")
        break
if not flag:
    print("Account Locked")