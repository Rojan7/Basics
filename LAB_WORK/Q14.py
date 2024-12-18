#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter
class Circle :
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius

c1 = Circle(5)
print(c1.area())
print(c1.perimeter())

c2 =Circle(6)
print(c2.area())
print(c2.perimeter())