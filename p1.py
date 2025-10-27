class rectangle():
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
		
	def area(self):
		area1=self.length*self.breadth
		return area1
		
	def perimeter(self):
		perimeter=2*(self.length+self.breadth)
		return perimeter
		
r1=rectangle(20,34)
area1=r1.area()
perimeter=r1.perimeter()
print("Area of rectangle 1:",area1)
print("Perimeter of rectangle 1:",perimeter)

r2=rectangle(5,34)
area2=r2.area()
perimeter=r2.perimeter()
print("Area of rectangle 2:",area2)
print("Perimeter of rectangle 2:",perimeter)



if(area1>area2):
	print(f"First rectangle is greater (area={area1})")
else:
	print(f"Second rectangle is greater (area={area2})")
	