import time, math

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

digitList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
panList = []
found = True
pan = 0
time1 = time.time()

for sInd in range(len(digitList)):
	tempList = digitList[:-sInd]
	for i in range(1, int(math.pow(10, len(tempList))), 2):
		ind = i

		strI = str(ind)
		found = True
		for d in tempList:
			if d not in strI:
				found = False
				break

		if found and ind > pan:
			if isPrime(ind):
				print(ind)
				pan = ind

print(time.time() - time1)

print(pan)
quit()

print()
print(panList)
time.sleep(4)

maxPan = 123456789
pCount = 0
for p in panList:
	pCount += 1
	print(pCount)
	if p > maxPan and isPrime(p):
		maxPan = p

print(maxPan)