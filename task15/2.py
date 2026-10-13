'''Instance methods: Rectangle area and perimeter
Problem: Create a Rectangle class with length and breadth. 
         Use instance methods to calculate its area and perimeter.'''


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)


length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
rectangle = Rectangle(length, breadth)
print("Area of the rectangle: ", rectangle.area())
print("Perimeter of the rectangle: ", rectangle.perimeter())
