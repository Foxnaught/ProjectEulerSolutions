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

def newCoprime(n):
	numList = list(range(n+1))

	for p in SOE(n):
		if p > n:
			break
		#For every prime that divides n, cancel all its multiples
		if not n % p:
			numList[p] = 0
			mult = 2
			while p * mult <= n:
				numList[p*mult] = 0
				mult += 1

	coprimes = []
	#For every value that wasn't canceled, put it in the coprime array
	for c in numList:
		if c != 0:
			coprimes.append(c)

	return coprimes



total = 1000000
#total = 10
numbers = list(range(total + 1))

highRatio = 0
highN = 0
currentMult = 1
for n in SOE(total+1):
	currentMult = currentMult * n

	if currentMult > total:
		break

	coprimes = newCoprime(currentMult)
	newRatio = currentMult/len(coprimes)
	if newRatio > highRatio:
		highN = currentMult
		highRatio = newRatio

print(highRatio)
print(highN)







