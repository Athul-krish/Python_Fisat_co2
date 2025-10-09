word=input("Enter a string:")
count = {}
for c in word:
    count[c] = count.get(c, 0) + 1

print(count)

