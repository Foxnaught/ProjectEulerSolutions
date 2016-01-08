import time

def factorSum(n):
	factors = []
	fSum = 0
	for i in range(1, int(n/2)+1):
		if(i not in factors):
			if n % i == 0:
				factors.append(i)
				#Don't save n only save lesser divisors
				if i != 1 and n != i*i:
					factors.append(int(n/i))

	for i in factors:
		fSum += i

	return fSum

startTime = time.time()

amicableList = []
n = int(input("input range: "))

#Were skipping primes because they don't have amicability with any other number
#Start at 4 to skip 1, 2 and 3
for i in range(n):
	#keep track of our progress
	if(i % 100 == 0):
		print(i)

	#This gives b
	b = factorSum(i)
	#If it's amicable a will be i
	a = factorSum(b)
	if(a == i != b):
		if(a not in amicableList):
			amicableList.append(a)
		if(b not in amicableList):
			amicableList.append(b)

totalSum = 0
for a in amicableList:
	totalSum += a

print(totalSum)


endTime = time.time() - startTime

print(endTime)