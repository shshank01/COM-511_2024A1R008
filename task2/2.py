# To calculate simple interest and total amount using principal, Rate, and Time entered by the user.

princ = int(input("Enter the pricipal: "))
rate = float(input("Enter the rate: "))
time = int(input("Enter the time: "))
simple_interest = (princ * rate * time) / 100
total_amount = princ + simple_interest
print("Simple Interest: ", simple_interest)
print("Total amount: ", total_amount)
