def SOE(n):
	numList = list(range(n))
	numList[1] = 0
	primeList = [2]

	for i in range(3, n, 2):
		if numList[i] != 0:
			primeList.append(i)
			for t in range(2, int(n/2)):
				if t*i < n:
					numList[t*i] = 0
				else:
					break

	return primeLis

#Start
n = int(input("Prime limit: "))

permPrimes = SOE(n)
permLen = len(permPrimes)
index = 0
maxPSum = 0
maxPCount = 0
print(permLen)
pSum = 0
primes = permPrimes[:]
while index < permLen:
	if not index % 100:
		print(index)

	pSum = 0
	pCount = 0
	for p in primes:
		pSum += p
		pCount += 1

		if pCount > maxPCount and pSum < n and pSum in primes:
			maxPSum = pSum
			maxPCount = pCount

	primes.pop(0)
	index += 1

print()
print(maxPCount)
print(maxPSum)