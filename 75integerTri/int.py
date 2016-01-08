import math
from copy import deepcopy

def getSquares(n):
	squareList = []
	for i in range(0, n):
		if i*i > n:
			break

		squareList.append(i*i)

	return squareList


def SOE(n):
	numList = list(range(n))
	primes = [2]
	for i in range(3, n, 2):
		if numList[i]:
			primes.append(i)

			mult = 3
			while i * mult < n:
				numList[i*mult] = 0
				mult += 2

	return primes


limit = 1500000
#limit = 48

primes = SOE(limit)

lenList = list(range(0, limit+1))
for l in range(len(lenList)):
	lenList[l] = -1


for p in primes[3:]:
	mult = 1
	while mult * p <= limit:
		lenList[mult * p] = 0
		mult += 1

for i in range(12, limit+1):#1500000+1):
	if not i % 1000:
		print(i)

	if lenList[i] == -1:
		triFound = False
		composite = False

		for a in range(1, i):
			for b in range(a, i-a):
				if i == a + b + math.sqrt(a*a+b*b):
					if triFound:
						composite = True
						mult = 1
						while mult * i <= limit:
							lenList[mult * i] = 0
							mult += 1

						break

					else:
						triFound = True

			if composite:
				break

		if triFound:
			mult = 1
			while mult * i <= limit:
				lenList[mult * i] = 1
				mult += 1
		else:
			lenList[i] = 0


cSum = 0
for x in range(12, limit+1):
	if lenList[x] == 1:
		cSum += 1

print(cSum)


