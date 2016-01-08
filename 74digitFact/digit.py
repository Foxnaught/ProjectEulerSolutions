
def factorial(n):
	mult = 1

	i = n
	while i:
		mult = mult * i
		i -= 1

	return mult


count = 0
for number in range(1, 1000000):
	if not number % 1000:
		print(number)

	nList = [number]
	while 1:
		fSum = 0
		for c in str(number):
			fSum += factorial(int(c))

		if fSum not in nList:
			nList.append(fSum)
			number = fSum
		else:
			break

	if len(nList) == 60:
		count += 1
		print(count)

print(count)