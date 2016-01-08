def SOE(n):
	numList = list(range(n))
	numList[1] = 0
	primeList = [2]

	for i in range(3, n, 2):
		if numList[i] != 0:
			primeList.append(i)
			for t in range(2, int(n/2)):
				if t*i < n:
					numList[t*i] = 0
				else:
					break

	return primeList

def getUniques(listArg):
	return list(set(listArg))

def getUnique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def getPrimeFactors(num):
	factorList = []
	newNum = num
	#foundFactor = True
	#If nothing sets foundFactor back to true then there is nothing more we can do (newNum == 1)
	while 1:
		#foundFactor = False
		tempList = [2] + list(range(3, int((newNum+1)/2), 2)) + [newNum]
		for i in tempList:
			if newNum % i == 0:
				factorList.append(i)
				newNum = int(newNum/i)
				if newNum == 1:
					return factorList

				#foundFactor = True
				break

	return factorList


#expand available prime list as necessary. This seems like a sufficient number of primes to work with.
#pList = SOE(1000000)
#number of consecutive numbers with number of distinct prime factors
n = int(input("n: "))

belt = []
#Stored values for the number of unique primes
storedB = []
nextNum = 2
for i in range(n):
	belt.append(nextNum)
	storedB.append(len(getUnique(getPrimeFactors(nextNum))))
	nextNum + 1

rN = range(n)
rNLess = range(n-1)
while 1:
	badSequence = False

	for b in rN:
		if storedB[b] != n:
			badSequence = True
			break

	if badSequence:
		for i in rNLess:
			#belt[i] = belt[i+1]
			storedB[i] = storedB[i+1]

		#belt[-1] = nextNum
		storedB[-1] = len(getUnique(getPrimeFactors(nextNum)))
		nextNum += 1
		
		if not nextNum % 1000:
			print(nextNum)
	else:
		break


print(nextNum - 2)
print(getUnique(getPrimeFactors(nextNum-2)))
print(nextNum - 3)
print(getUnique(getPrimeFactors(nextNum-3)))
print(nextNum - 4)
print(getUnique(getPrimeFactors(nextNum-4)))


