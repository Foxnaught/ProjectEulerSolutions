def factorSum(n):
	fSum = 0
	factorList = []
	for i in range(1, int(n/2)+1):
		if i not in factorList:
			if n % i == 0 and n != i:
				secondFactor = int(n/i)
				factorList.append(i)
				fSum += i
				#Don't save n only save lesser divisors
				#Also don't save i twice (if n is i squared then the second factor is also i)
				if i != 1 and secondFactor not in factorList:
					fSum += secondFactor
					factorList.append(int(n/i))

	return fSum

def findAbundant(allNum):
	abundant = []
	for i in allNum:
		if factorSum(i) > i:
			abundant.append(i)

	return abundant

#Half of 28123
n = 28123

allNum = []
for i in range(1, n):
	allNum.append(i)


abundant = findAbundant(allNum)

#See how long this is going to take us
print(len(abundant))

count = 0
for i in abundant:
	#Show where we are
	count += 1
	if count % 100 == 0:
		print(count)

	for t in abundant:
		if i+t <= n-1 and allNum[i+t-1] != 0:
			allNum[i+t-1] = 0

nonabundant = []
totalSum = 0
for num in allNum:
	if num != 0:
		nonabundant.append(num)
		totalSum += num

print(nonabundant)
print(totalSum)


