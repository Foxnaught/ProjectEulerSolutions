import math

#n must be odd
def isPrime(n):
	for i in range(3,int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False

	return True

def SOE(n):
	numList = list(range(n))
	primeList = [2]

	for i in range(3, n, 2):
		if numList[i] != 0:
			primeList.append(i)
			for t in range(i, int(n/i)+1, 2):
				if t*i < n:
					numList[t*i] = 0
				else:
					break

	return primeList

def sumOfPrimeAndSquare(n):
	primeList = SOE(n)

	for i in range(int(math.sqrt(n)) + 1):
		for p in primeList:
			if n == p + 2*i*i:
				return True

	return False


oddComps = []
n = 1000000
primes = SOE(n)
numberList = list(range(3, n, 2))

for i in range(3, n, 2):
	if not isPrime(i):
		if not sumOfPrimeAndSquare(i):
			print(i)
			quit()

print("fail")








