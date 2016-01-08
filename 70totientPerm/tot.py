import math, time

#This is a failed attempt
#It's algorithms are useful

#b must be smaller than a
def gcd(a, b):
	while b:
		temp = a % b
		a = b
		b = temp

	return a

def phi(n):
	count = 0

	for i in range(1, n):
		if gcd(n, i) == 1:
			count += 1

	return count

def isPerm(a, b):
	return sorted(a) == sorted(b)

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

def primeFactors(n):
	global primes
	#One is not a valid prime factors but it simplifies the algorithm, we strip it out when we return the list
	factors = []
	last = 0
	i = 0
	while n != 1:
		if not n % primes[i]:
			n = n/primes[i]

			if primes[i] != last:
				factors.append(primes[i])
				last = primes[i]
		else:
			i += 1

	return factors

def stackTime(timeStack, time):
	for i in reversed(range(len(timeStack)-1)):
		timeStack[i+1] = timeStack[i]

	timeStack[0] = time

	return timeStack

def timeAverage(timeStack):
	timeSum = 0
	for i in timeStack:
		timeSum += i

	return timeSum/len(timeStack)


primes = SOE(11000000)


minRatio = 2
lowN = 1
timeCache = [20]*20
mark = time.time()
totient = 0
for i in reversed(range(3, 10000000, 2)):# range(1, 10000000, 2):
	if not (i-1) % 1000:
		print(i-1)
		diff = time.time() - mark
		print(diff)
		mark = time.time()
		stackTime(timeCache, diff)
		print(timeAverage(timeCache))
		


	totient = i
	for p in primeFactors(i):
		totient = totient * (1-1/p)

	if i/totient < minRatio and sorted(str(i)) == sorted(str(totient)):
		minRatio = i/totient
		print(i)
		print(totient)
		lowN = i

print(lowN)






