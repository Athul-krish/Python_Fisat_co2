f1 = open("source.txt", "r")
f2 = open("target.txt", "w")
lines = f1.readlines()
for i in range(0, len(lines)):
	if i % 2 == 0:
		f2.write(lines[i])
f1.close()
f2.close()
