# To ask the user for radius and calculate area and circumference of a circle
import math
r = float(input("Enter the radius: "))
print("Area of circle: ", round(math.pi*r*r,2))
print("Circumference of circle: ", round(2*math.pi*r,2))
