import time

def recurseSumArray(nList, index=0, mainLine=[]):
	arrayList = []
	totalList = []
	numberList = []
	for n in range(index, len(nList)):
		if nList[n] not in numberList:
			numberList.append(nList[n])
			for i in range(1, nList[n]):
				first = []
				if i - 1 >= 0:
					first = nList[:n]

				sumArray = sorted(first + nList[n+1:] + [nList[n] - i, i])

				totalList = arrayList + mainLine
				if sumArray not in totalList:
					arrayList.append(sumArray)
				
					for t in recurseSumArray(sumArray, n+1, totalList):
						#if t not in arrayList + mainLine:
						arrayList.append(t)


	return arrayList


startTime = time.time()
unique = []
print(len(recurseSumArray([int(input("Value: "))])))
print("Time: " + str(time.time() - startTime))