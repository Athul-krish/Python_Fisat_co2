a=0
b=1
num=int(input("Enter a number:"))
for i in range(num):
	print(a,end=" ")
	c=a+b
	a=b
	b=c
	
print()	
