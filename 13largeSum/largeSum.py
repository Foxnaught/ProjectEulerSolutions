
f = open("digits.txt")

text = ""
largeSum = 0
text = f.readline()
while(text.__len__() > 0):
	largeSum += int(text)
	text = f.readline()

print(largeSum)
