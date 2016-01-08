import time, math

#For a given value of x and n in the equation 1/x + 1/y = 1/n
#return y or -1 if y is not an integer
def findY(x, n):
	attempt = round(1/(1/n - 1/x))
	if(1/x + 1/attempt == 1/n):
		return attempt
	else:
		return -1


def gcd(a, b):
	if a < b:
		#swap
		temp = a
		a = b
		b = temp

	while(a % b):
		#swap
		temp = a % b
		a = b
		b = temp

	return b


def pow(a, b):
	mult = 1
	for i in range(b):
		mult *= a

	return mult

def factorCount(n):
	count = 0
	for i in range(2, int(n/2)+1):
		if not n % i:
			count += 1

	return count

def getCoprimes(n):
	count = 0
	i = 1
	while i*i <= n:
		if not n % i and (gcd(n/i, i) == 1 or n/i == i):
			count += 1

		i += 1

	return count

def isPrime(n):
	if pow(2, n-1) % n == 1:
		return True

	return False

def getPrimes(n):
	count = 0
	i = 2
	while n > 1:
		if not n % i:
			n = n/i
			count += 1
		else:
			i += 1

	return count

def SOE(n):
	primeList = [2]
	numList = list(range(0, n+1))
	for i in range(3, n+1, 2):
		if numList[i]:
			primeList.append(i)
			for t in range(3, int(n/i)+1, 2):
				numList[i*t] = 0

	return primeList

#We will iterate through the 
#starting n value
n = 4
#We know it has to be higher than this n from previous runs
#n = 180000
largestCount = 0
largestfNum = 0
start = time.time()
xList = []
nMax = 2
bigD = 1
nMaxSquared = nMax*nMax

largestFNum = 0
while 1:
	count = 2
	#inverseN = 1/n
	nSquared = n*n

	#Not sure why this works but it does. Comparing the GCD of the squares vs the GCD of the unsquared values filters out unwanted n values
	if gcd(nSquared, nMaxSquared) > bigD:
		for x in range(2, n):
			if not nSquared % x:
				count += 1


	if count > 4000000:
		break
	elif count > largestCount:
		largestCount = count
		bigD = gcd(n, nMax)
		nMax = n
		nMaxSquared = nMax * nMax

	if n % 1000 == 0:
		print(n)
		print(largestCount)
		print("Time: " + str(time.time() - start))
		start = time.time()
		

	n += 1

print(count)
print(n)


