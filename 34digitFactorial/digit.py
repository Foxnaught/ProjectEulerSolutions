def fact(n):
	mult = 1
	for i in range(2, n+1):
		mult = mult * i

	return mult

factList = []
strSum = 0
strVal = ''
for i in range(1, 10000000):
	if not i % 100000:
		print(i)

	strVal = str(i)
	strSum = 0
	for s in strVal:
		strSum += fact(int(s))

	if strSum == i:
		factList.append(i)

print(factList)