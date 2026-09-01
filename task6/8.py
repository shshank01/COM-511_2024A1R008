'''Write a python program to take an email address and print the domain name.'''
email = input("Enter your email address: ")
index = email.find('@')
domain = email[index+1:]
# domain=email.split('@')[1]
print(domain)
