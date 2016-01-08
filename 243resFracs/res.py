import math, time

#This is a failed attempt
#It's algorithms are useful

def gcd(a, b):
	#If b is bigger than a, do a XOR swap
	if a < b:
		a = a ^ b
		b = a ^ b
		a = a ^ b

	while b:
		temp = a % b
		a = b
		b = temp

	return a

def phi(n):
	count = 0

	if n == 1:
		count = 1

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

def totRec(n, nTot, header=0, chain=[]):
	global primes
	global primeLen
	global limit
	minP = False
	pTot = False
	#Each level exhaustes all multiples of a given prime
	#So the next level can skip all primes before it
	for i in range(header, primeLen - header):
		p = primes[i]
		#Basic case, we are still below the limit so let's check if this multiple and it's totient have a lower ratio and are pandigital to each other
		if (not minP or (n*p)/(nTot * (p-1)) < minP/pTot) and gcd(n, p) == 1:
			minP = n * p
			pTot = nTot * (p-1)

			if pTot/minP < (4/10):#15499/94744:
				return [minP, pTot]

			#Recursive call
			if len(chain) < 15:
				permVal = totRec(n * p, nTot * (p-1), i+1, chain + [p])

				#If we found more pandigital multiples below the limit in the recursive call then let's check if it has a lower ratio than what we can currently see
				if permVal[0]:
					if (not minP or permVal[1]/permVal[0] > pTot/minP) and permVal[1]/permVal[0] < (4/10):#15499/94744:
						minP = permVal[0]
						pTot = permVal[1]
						return [minP, pTot]

		
	#pass the n value and it's totient that has the lowest ratio on this level
	#returns false in both values if no pandigital ratio is found
	return [False, False]

def primeFactors(n):
	factors = []
	last = 0
	i = 2
	while n != 1:
		if not n % i:
			n = n/i

			if i != last:
				factors.append(i)
				last = i
		else:
			i += 1

	return factors

def nextSum(nList):
	i = 0
	while 1:
		if i not in nList:
			nList.append(i)
			break
		else:
			del nList[nList.index(i)]

		i += 1

	return nList

def appendPrime(nList):
	nList = sorted(nList)

	for i in range(nList[-1]):
		if i not in nList:
			return sorted(nList + [i])

	return sorted(nList + [nList[-1]+1])

def compress(nList):
	global primes

	nList = sorted(nList)
	nextPrime = primes[nList[-1]+1]

	for i in range(1, nList[-1]):
		if i not in nList:
			nextPrime = i
			break


	sumList = [0]
	while 1:
		pSum = 0
		for p in sumList:
			if p >= len(nList):
				return False
			pSum += primes[nList[p]]

		if pSum > nextPrime:
			return [i for j, i in enumerate(nList) if j not in sumList] + [nextPrime]

		sumList = nextSum(sumList)

def recPrimeList(numList, nTot, header=0):
	global primes
	global lowN
	global toBeat
	global limit

	mult = 1
	for n in numList:
		mult *= n

	if (mult <= lowN):
		totient = mult
		for p in primeFactors(mult):
			totient *= (1-1/p)

		if (mult > 1 and totient/(mult-1) < toBeat):
			lowN = mult
			print(lowN)

		for p in range(header, len(primes)):
			recPrimeList(numList+[primes[p]], totient, p)


#fairly efficient trial division
def testFact(n):
	factors = []

	if not n % 2:
		n = n / 2
		factors.append(2)
		while not n % 2:
			n = n / 2


	i = 3
	while i < math.sqrt(n):
		if not n % i:
			n = n / i
			factors.append(i)
			while not n % i:
				n = n / i

		i += 2

	if n != 1:
		factors.append(n)

	return factors



#primes = SOE(9000000)
#print("Ready")

#This value has a ratio less than our target but it is not the correct answer
limit = 6469693230
lowN = limit
nTot = limit
for p in primeFactors(limit):
	nTot *= (1-1/p)
toBeat = 15449/94744
#toBeat = 4/10

lowIter = 2
lowRes = 0
i = limit - (2+3+5+7+11+13+17)
while 1:
	if not i % 10000:
		print(i)

	totient = i
	for p in testFact(i):
		totient *= (1-1/p)

	if not lowRes or totient/(i-1) < lowRes/(lowIter-1):
		lowRes = totient
		lowIter = i
		print("Found!")
		print(i)
		print("Ratio: " + str(lowRes/(lowIter-1)))
		print("To Beat: " + str(toBeat))

		if lowRes/(lowIter-1) < toBeat:
			exit()

	i -= (2+3+5+7+11+13+17)




