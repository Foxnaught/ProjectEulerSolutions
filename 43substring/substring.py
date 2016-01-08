import time


#Takes in a pandigital number in string form and determines the next pandigital greater than the input
def nextPan(strN):
	intInd = 0
	strN = list(strN)
	for i in range(2, len(strN)+1):
		intInd = int(strN[-i])

		offset = 1
		remainder = strN[-i+1:]
		
		while intInd+offset <= 9:
			for c in range(len(remainder)):
				if str(intInd + offset) == remainder[c]:
					del remainder[c]
					remainder.append(str(intInd))
					remainder = sorted(remainder)

					#Return out next pandigital
					return strN[:-i] + [str(intInd + offset)] + remainder

			offset += 1

	#There is no next pandigital
	return False


panList = []
time1 = time.time()
curPan = "1023456789"
while curPan:
	strI = curPan

	if not int(strI[7:10]) % 17:
		if not int(strI[6:9]) % 13:
			if not int(strI[5:8]) % 11:
				if not int(strI[4:7]) % 7:
					if not int(strI[3:6]) % 5:
						if not int(strI[2:5]) % 3:
							if not int(strI[1:4]) % 2:
								panList.append(curPan)
								print(curPan)

	curPan = nextPan(curPan)
	if curPan:
		curPan = ''.join(curPan)

print(time.time() - time1)
pSum = 0
for p in panList:
	pSum += int(p)

print(pSum)