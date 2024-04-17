

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
