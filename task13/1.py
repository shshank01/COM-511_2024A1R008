# Write a python program to store two points as tuples and calculate the distance between them
import math
x1,y1=map(int,input("Enter two points: ").split())
x2,y2=map(int,input("Enter two points: ").split())
print("Distance between two points: ", math.sqrt((x2-x1)**2+(y2-y1)**2))