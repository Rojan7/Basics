#Implement a class Shape with a method area() which returns 0. Then, create subclasses
#Rectangle and Circle. Overload the area() method in both subclasses to calculate and return
#the area of a rectangle and a circle respectively.

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):    # super().area() can also be done if we do not want to overwrite the area method
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(5, 3)
circle = Circle(2)

print("Area of Rectangle:", rectangle.area())
print("Area of Circle:", circle.area())