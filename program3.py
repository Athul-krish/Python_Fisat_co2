num=[]
 
for i in range(5):
	a=int(input("Enter number:"))
	num.append(a)

sum=0	
for i in num:
	sum=sum+i
	i=i+1
	
print("The sum of list is :",sum)


