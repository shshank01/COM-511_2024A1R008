# Write a python program to calculate the final bill amount after applying a discount.
# The program should take the total bill amount as input from the user and apply the discount according to the following rules.
# After calculating the discount, the program should display the discount amount and the final bill amount payable to the customer.
# Bill Amount    Discount
# Above 5000      20%
# 3000-5000       10%
# Below 3000      No discont

bill=int(input("Enter the total bill amount: "))
if bill>5000:
    discount=bill*0.2
    final_bill=bill-discount
    print("Discount amount: ",discount)
    print("Final bill amount payable: ",final_bill)
elif bill >=3000 and bill<=5000:
    discount=bill*0.1
    final_bill=bill-discount
    print("Discount amount: ",discount)
    print("Final bill amount payable: ",final_bill)
else:
    print("No discount applicable.")
    print("Final bill amount payable: ",bill)