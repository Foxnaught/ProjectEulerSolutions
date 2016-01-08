


#b must be smaller than a
def gcd(a, b):
	while b:
		a = a % b

		a = a ^ b
		b = a ^ b
		a = a ^ b

	return a

def phi(n):
	count = 0

	for i in range(1, n):
		if gcd(n, i) == 1:
			count += 1

	return count

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

primes = SOE(1100000)

"""
t = 54739
print(phi(t))
cSum = t
for p in primeFactors(t):
	cSum = cSum * (1-1/p)
print(cSum)
exit()
"""

limit = 1000000
limit = 100000
cSum = 0
for i in reversed(range(2, limit+1)):
	if not i % 1000:
		print(i)

	totient = i
	for p in primeFactors(i):
		totient = totient * (1-1/p)

	cSum += totient

print(cSum)
