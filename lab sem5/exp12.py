# Function to find the largest of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)


# Function to check Armstrong number
def is_armstrong(n):
    temp = n
    digits = len(str(n))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if sum == n:
        return True
    else:
        return False


# Main program
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest number:", max_of_three(a, b, c))

n = int(input("Enter a number to check Armstrong: "))

if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
