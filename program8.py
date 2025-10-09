words=[]
num=int(input("Enter the limit:"))
for i in range(num):
	word=input("Enter string:")
	words.append(word)
	
l=0	
for i in words:
	if len(i)>l:
		l=len(i)
	
print("Length of longest word is:",l)	
