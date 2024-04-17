# Ques) Write a python class named Rectangle to represent a rectangle shape. The class should have the following functionalities:
# 1 -> A method named set_dimensions that takes two parameters width and height and set the attributes of the rectangle accordingly.
# 2 -> A method named area that calculates and returns the area of the rectangle.
# 3 -> A method named perimeter that calculates and returns the perimeter of the rectangle.
# use this to  create objects of the class and print width, height, area and perimeter.
# Solution-

class Rectangle:
	def __init__(self,length,width):
		self.length = length
		self.width = width

	def area(self):
		return self.length * self.width

	def perimeter(self):
		return 2 * (self.length + self.width)

rectangle1=Rectangle(4,5)
rectangle2=Rectangle(10,14)
rectangle3=Rectangle(8,4)
print("Length of rectangle1 :",rectangle1.length)
print("Width of rectangle1 :",rectangle1.width)
print("Area of rectangle1 :",rectangle1.area())
print("Perimeter of rectangle1 :",rectangle1.perimeter())
