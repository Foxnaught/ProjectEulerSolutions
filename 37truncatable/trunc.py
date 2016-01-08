import time

def SOE(n):
	primeList = [2]
	numList = list(range(0, n+1))

	for i in range(3, n+1, 2):
		if numList[i] != 0:
			primeList.append(i)

			for t in range(3, int(n/i)+1, 2):
				numList[i*t] = 0

	return primeList

#Just enough to find all the primes.
#Started with 1000000 and reduced from there
primes = SOE(750000)

i = 8
count = 0
primeSum = 0

while(count < 11):
	found = True

	strPrime = str(primes[i])
	primeLen = len(strPrime)-1
	for n in range(primeLen):
		if int(strPrime[:n+1]) not in primes:
			found = False
			break

	if found:
		for n in range(primeLen):
			if int(strPrime[-n-1:]) not in primes:
				found = False
				break

		if found:
			count += 1
			primeSum += primes[i]
			print(primes[i])

	i += 1


print("Prime sum:" + str(primeSum))