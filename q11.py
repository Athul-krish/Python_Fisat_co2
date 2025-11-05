area_square = lambda x:print(f"Area of square is {x*x}") 
n=int(input("Enter a side : "))
area_square(n)

area_rectangle = lambda l,w:print(f"Area of rectangle is {l*w}")
l=int(input("Enter length : "))
w=int(input("Enter width : "))
area_rectangle(l,w)

area_triangle = lambda b,h:print(f"Area of triangle is {0.5*b*h}")
h=int(input("Enter height : "))
b=int(input("Enter breadth : "))
area_triangle(b,h)
