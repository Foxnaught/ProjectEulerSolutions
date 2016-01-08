import math

def getTriangle(n):
	return int((n*(n+1))/2)

def getPentagonal(n):
	return int(n*(3*n-1)/2)

def getHexagonal(n):
	return int(n*(2*n-1))


def isTri(n):
	temp = getTriIndex(n)

	return int(temp) == temp

def getTriIndex(n):
	return (math.sqrt(8*n + 1) - 1)/2


def isPent(n):
	temp = getPentIndex(n)

	return int(temp) == temp

def getPentIndex(n):
	return (math.sqrt(24 * n + 1) + 1)/6


def isHex(n):
	temp = getHexIndex(n)

	return int(temp) == temp

def getHexIndex(n):
	return (math.sqrt(16*n + 1) + 1)/4

hexIndex = 144
while 1:
	curHex = getHexagonal(hexIndex)

	if isPent(curHex):
		if isTri(curHex):
			break

	hexIndex += 1

print(curHex)
