import csv
data = [ {"Name": "Athul", "Age": 22}, {"Name": "Nikhil", "Age": 25} ]
with open("output.csv", "w", newline="") as f:
	writer = csv.DictWriter(f, fieldnames=["Name", "Age"])
	writer.writeheader()
	writer.writerows(data)
dict={1:"joice",2:"Anil"}
filehandler = open("fi", 'w+')
data = str(dict)
filehandler.write(data)
