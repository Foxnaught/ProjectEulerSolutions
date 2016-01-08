import math, time


def SOE(n):
	numList = list(range(n+1))
	primeList = [2]

	for i in range(3, n+1, 2):
		if numList[i] != 0:
			primeList.append(i)

			mult = 3
			while mult * i <= n:
				numList[mult * i] = 0
				mult += 2

	return primeList


primes = SOE(9000000)

def isPrime(n):
	if not n % 2:
		return False

	for i in range(3, int(math.sqrt(n))+1, 2):
		if not n % i:
			return False

	return True


for p in primes:
	print(p)
	strP = str(p)
	lenP = len(strP)

	#For any given digit
	for i in range(10):
		#We already know is has one form that is a prime: itself.
		count = 1
		#Count the number of times it appears in the prime
		strI = str(i)
		n = strP.count(strI)
		#If it occurs in the prime
		if n:
			#Replace it with every other number except the current one
			#Don't bother replacing with values less than the current digit values because those primes have already been checked this way.
			for t in range(i+1, 10):
				#Replace all instances of i with a new digit t
				newStr = strP.replace(strI, str(t))
				newInt = int(newStr)
				#If there are no leading zeros in the new number (same number of digits) and it's a prime then count up
				if len(str(newInt)) == lenP and isPrime(newInt):
					count += 1

		if count >= 8:
			print("Found!")
			print(p)
			exit()



