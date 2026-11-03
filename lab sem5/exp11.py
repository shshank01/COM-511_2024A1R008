import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check whether triangle is valid
if a + b > c and a + c > b and b + c > a:

    # Check right-angled triangle
    sides = sorted([a, b, c])

    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")

    # Heron's formula
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    print("Area of triangle:", area)

else:
    print("Invalid triangle")
