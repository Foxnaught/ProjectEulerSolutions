import math, time, copy

def pow(a, b):
	mult = 1
	for i in range(b):
		mult = mult * a

	return mult

def isBinary(n):
	while n > 1:
		n = n/2

	return n == 1

def getBinaryPow(n):
	i = 0
	while n > 1:
		n = n / 2
		i += 1

	return i

def maxBinary(n):
	curN = n
	i = 0
	sumList = []

	while curN > 0:
		if curN % 2:
			sumList.append(i)

		curN = int(curN / 2)

		i += 1

	return sumList

def minBinary(mBin):
	newBin = mBin[:]
	while 1:
		breakNum = -1
		for i in range(len(newBin)):
			if newBin[i] > 0:
				if newBin.count(newBin[i]-1) == 0:
					breakNum = newBin[i]
					break

		if breakNum == -1:
			break

		del newBin[i]
		newBin.append(breakNum-1)
		newBin.append(breakNum-1)
		newBin = sorted(newBin)


	return newBin

#limit is arbitrarily high
#Generally exponents won't be higher than 40
def pinch(nList, listLen, limit = 100000000000):
	combos = 1
	#cList = [nList]
	for n in range(listLen-1):
		if nList[n] <= limit:
			if nList[n] == nList[n+1] and (n > listLen - 4 or not nList[n+2] == nList[n+3] == nList[n]+1):#nList.count(nList[n]+1) <= 1:
				t = nList[:]
				del t[n]
				t[n] += 1

				combos += pinch(t, listLen-1, nList[n]+1)
				#cList.extend(pinch(t, listLen-1, nList[n]+1))

	return combos


n = pow(10, int(input("Power: ")))
print(n)
maxBin = maxBinary(n)
minBin = minBinary(maxBin)
mainList = [minBin]
start = time.time()
print(pinch(minBin, len(minBin)))

print(time.time() - start)
exit()

start = time.time()

totalList = []
tempList = []
buildList = [[minBin, -1]]
totalList = buildList
totalCount = 1
sorting = True
while sorting:
	sorting = False
	for b in buildList:
		curList = b[0]
		for i in range(len(curList)-1):
			if curList[i] <= b[1] or b[1] == -1:
				if curList[i] == curList[i+1] and curList.count(curList[i] + 1) <= 1:
					sorting = True
					t = curList[:]
					del t[i]
					t[i] = curList[i] + 1

					tempList.append([t, curList[i] + 1])
					totalCount += 1

	buildList = tempList
	tempList = []

print(totalCount)
print(time.time() - start)



exit()
print("trying degrade")

maxList = sorted(maxBinary(n))
print(maxList)

mainList = []
tempList = []
tempList2 = []
mainList.append(maxList)
tempList.append(maxList)

sorting = True
start = time.time()
add = False
next = 0
while sorting:
	sorting = False
	for i in tempList:
		iLen = len(i)
		for n in range(iLen):
			if i[n] > 0:
				#To devolve a item in the list it can be shown 2^4 = 2^3 + 2^3 therefore [4] turns into [3, 3], [3] turns into [2, 2] etc
				next = i[n] - 1

				#We cannot have more than 2 of a given exponent in a solution.
				#If the next exponent down already exists in the sum then devolving that item will cause at least 3 elements to be the same
				add = True
				if n > 0:
					if next == i[n-1] or (n > 1 and next == i[n-2]):
						add = False

				if n < iLen - 1:
					if next == i[n+1] or (n < iLen - 2 and next == i[n+2]):
						add = False

				if add:
					#t will be our copy of i with one element switched out for the next combination
					t = i[:]

					t[n] = next
					t.append(next)

					t = sorted(t)
					if t not in tempList + tempList2:
						sorting = True
						#mainList.append(t)
						tempList2.append(t)

	mainList.extend(tempList2)
	tempList = tempList2
	tempList2 = []

print(time.time() - start)

print(len(mainList))

"""

[3, 1]
[2, 2, 1]
[3. 0. 0]
[2, 2, 0, 0]
[2, 1, 1, 0, 0]

[3]
[2, 2]
[2, 1, 1]
[2, 1, 0, 0]

[4]
[3, 3]
[3, 2, 2]
[3, 2, 1, 1]
[3, 2, 1, 0, 0]


"""


