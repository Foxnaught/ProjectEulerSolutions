import math

def isPrime(n):
	prime = True
	for i in range(2, int(n/2)+1):
		if(n % i) == 0:
			prime = False
			break
	return prime

def generatePrimes(n):
	primeList = [2]
	for i in range(3, n-1):
		if i % 2 == 1:
			isPrime = True
			for prime in primeList:
				if i % prime == 0:
					isPrime = False
					break

			if isPrime:
				primeList.append(i)

	return primeList

largeAB = [0,0]
largeCount = 0

#Generates enough primes to work
primeList = generatePrimes(1700)


print("Done with primes")
prevCount = 0
savedAB = ()
#Where the formula breaks down
savedN = 0
for a in range(-1000, 1001):
	if(a % 100 == 0):
		print(a)

	for b in range(-1000, 1001):
		n = 0
		counter = 0
		while 1:
			counter += 1
			if (n*n + n*a + b) not in primeList:
				break

			n += 1

		if counter > prevCount:
			prevCount = counter
			savedAB = (a, b)
			savedN = n

print(savedAB)
print(savedN)