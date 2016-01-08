import math

def myPow(base, pow):
	returnValue = 1
	for i in range(pow):
		returnValue = returnValue * base

	return returnValue

digitString = str(myPow(2, 1000))
powerSum = 0
for i in range(digitString.__len__()):
	powerSum += int(digitString[i])

print(powerSum)



