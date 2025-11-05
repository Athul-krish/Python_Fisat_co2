class Rectangle:
	def __init__(self,length,width):
		self.__length = length
		self.__width = width
		
	def area(self):
		return self.__length*self.__width
		
	def __lt__(self, other):
		return self.area()<other.area() 
		
rect1 = Rectangle(30, 12)
rect2 = Rectangle(21, 80)

if rect1 < rect2:
	print("Rectangle 1 is smaller than Rectangle 2")
else:
	print("Rectangle 2 is smaller than Rectangle 1")
