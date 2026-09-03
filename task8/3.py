# Take an email address and print username, domain, and reversed domain.
email=input("Enter email: ")
index=email.find("@")
username=email[0:index]
domain=email[index+1:]
reversed=domain[::-1]
print("Username: ", username)
print("Domain: ", domain)
print("Reversed domain: ", reversed)