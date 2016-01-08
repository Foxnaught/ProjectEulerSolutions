import math

maxVal = int(math.pow(9, 5)*6)
fifthList = []

for i in range(2, maxVal):
	tempSum = 0
	for t in str(i):
		tempSum += math.pow(int(t), 5)

	if tempSum == i:
		fifthList.append(i)

print(fifthList)
endSum = 0
for i in fifthList:
	endSum += i

print(endSum)
