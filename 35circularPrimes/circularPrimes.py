import math
import time

#Old trial division function
def generatePrimes(n):
	primeList = [2]
	isPrime = True
	for i in range(3, n, 2):
		if(i % 10001 == 0):
			print(i)

		isPrime = True
		for prime in primeList:
			if i % prime == 0:
				isPrime = False
				break

		if isPrime:
			primeList.append(i)

	return primeList

#faster sieve algorithm
def sieveOfEratosthenes(num):
	nonprimes = []
	primes = []

	n = num + 1
	for i in range(n+1):
		nonprimes.append(i)

	i = 2
	while 1:

		divisibleLimit = math.ceil((n)/i) - ((n)%i > 0) + 1
		for t in range(2, divisibleLimit):
			if(nonprimes[i*t] != 0):
				nonprimes[i*t] = 0

		found = False
		for item in range(i+1, len(nonprimes)):
			if nonprimes[item] != 0:
				found = True
				i = nonprimes[item]
				break

		if not found or i*i > num:
			break


	for i in range(2, len(nonprimes)):
		if nonprimes[i] != 0:
			primes.append(nonprimes[i])

	return primes


def circPrime(n, primes):
	tempNum = ""
	tempString = ""
	toInt = 0
	strNum = str(n)
	strLen = len(strNum)
	#Will hold the new rotations as we make them
	numList = [0] * strLen

	strRange = range(strLen)
	#exclude i=0 because that would give us the initial arrangement of the prime number
	#Since n should already be prime this would be wasted processing time
	for i in strRange[1:]:
		for s in strRange:
			numList[(s+i)%strLen] = strNum[s]

		tempString = ""
		for i in numList:
			tempString += i

		toInt = int(tempString)
		for t in primes:
			if toInt % t == 0 and t != toInt:
				return False

	return True

n = int(input("Max range: "))
startSieve = time.time()
#This value is globally used in circPrime
primes = sieveOfEratosthenes(n)
endSieve = time.time() - startSieve
print("Sieve complete: " + str(endSieve))


print(len(primes))

count = 0
for i in range(len(primes)):
	if(circPrime(primes[i], primes)):
		count += 1

print(count)



