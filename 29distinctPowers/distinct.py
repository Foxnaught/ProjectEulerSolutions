import math

n = 100

multList = []
for a in range(2, n+1):
	for b in range(2, n+1):
		tempVal = math.pow(a, b)
		if tempVal not in multList:
			multList.append(tempVal)

sorted(multList)

print(len(multList))