def factorial(n):
	product = 1
	for i in range(2, n+1):
		product = product * i

	return product


fSum = 0
for i in str(factorial(100)):
	fSum += int(i)

print(fSum)




