singleDigits = []
for n in range(1,10):
	singleDigits.append(str(n))

productList = []
i = 0

for a in range(999):
	aString = str(a)
	aLen = aString.__len__()
	print(a)
	for b in range(9999):
		bString = str(b)
		i = a*b
		iString = str(i)

		if iString.__len__() + aLen + bString.__len__() == 9:
			tempDigits = sorted(list(iString + aString + bString))
			if tempDigits == singleDigits and i not in productList:
				productList.append(i)

print(productList)
tSum = 0
for p in productList:
	tSum += p

print(tSum)