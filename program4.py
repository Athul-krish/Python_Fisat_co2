import math

start=int(input("Enter the start number : "))
end=int(input("Enter the end number : "))
if(start<1000):
	start=1000
if(end>10000):
	end=9998
if(end%2!=0):
	end=end+1
if(start%2!=0):
	start=start+1
	
for i in range(start,end+1,2):
	flag=False
	root=math.isqrt(i)
	for j in str(i):
		if int(j)%2!=0:
			flag=True
	if(i==root*root):
		if not flag:
			print(i)
	

