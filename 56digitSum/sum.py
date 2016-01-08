def power(a, b):
	mult = 1
	for i in range(b):
		mult = mult * a

	return mult

maxSum = 0
for a in range(100):
	for b in range(100):
		tempSum = 0
		strVal = str(power(a,b))

		for s in strVal:
			tempSum += int(s)

		if tempSum > maxSum:
			maxSum = tempSum

print(maxSum)