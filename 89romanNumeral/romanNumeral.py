
def calcRome(numeral):
	rSum = 0
	subBuf = 0
	bufChar = '0'
	for i in range(len(numeral)):
		if numeral[i] == 'M':
			rSum += 1000

			if bufChar == 'C':
				bufChar = '0'
				rSum -= subBuf
				subBuf = 0
		elif numeral[i] == 'D':
			rSum += 500
			if bufChar == 'C':
				bufChar = '0'
				rSum -= subBuf
				subBuf = 0
		elif numeral[i] == 'C':
			if bufChar == 'X':
				rSum -= subBuf
				subBuf = 0
			elif bufChar != 'C' and subBuf:
				rSum += subBuf
				subBuf = 0

			subBuf += 100
			bufChar = 'C'
		elif numeral[i] == 'L':
			rSum += 50

			if bufChar == 'X':
				bufChar = '0'
				rSum -= subBuf
				subBuf = 0
		elif numeral[i] == 'X':
			if bufChar == 'I':
				bufChar = '0'
				rSum -= subBuf
				subBuf = 0
			elif bufChar != 'X' and subBuf:
				bufChar = '0'
				rSum += subBuf
				subBuf = 0

			subBuf += 10
			bufChar = 'X'
		elif numeral[i] == 'V':
			rSum += 5

			if bufChar == 'I':
				bufChar = '0'
				rSum -= subBuf
				subBuf = 0
			elif subBuf:
				bufChar = '0'
				rSum += subBuf
				subBuf = 0
		elif numeral[i] == 'I':
			if bufChar != 'I' and subBuf:
				rSum += subBuf
				subBuf = 0

			subBuf += 1
			bufChar = 'I'

	return rSum + subBuf

def printRome(n):
	strN = str(n)
	numeral = ""

	if int(strN[-1]) == 9:
		numeral = "IX"
	elif int(strN[-1]) == 8:
		numeral = "VIII"
	elif int(strN[-1]) == 7:
		numeral = "VII"
	elif int(strN[-1]) == 6:
		numeral = "VI"
	elif int(strN[-1]) == 5:
		numeral = "V"
	elif int(strN[-1]) == 4:
		numeral = "IV"
	else:
		for i in range(int(strN[-1])):
			numeral += "I"

	if len(strN) > 1:
		buff = ""
		if int(strN[-2]) == 9:
			buff = "XC"
		elif int(strN[-2]) == 8:
			buff = "LXXX"
		elif int(strN[-2]) == 7:
			buff = "LXX"
		elif int(strN[-2]) == 6:
			buff = "LX"
		elif int(strN[-2]) == 5:
			buff = "L"
		elif int(strN[-2]) == 4:
			buff = "XL"
		else:
			for i in range(int(strN[-2])):
				buff += "X"

		numeral = buff + numeral

		if len(strN) > 2:
			buff = ""

			if int(strN[-3]) == 9:
				buff = "CM"
			elif int(strN[-3]) == 8:
				buff = "DCCC"
			elif int(strN[-3]) == 7:
				buff = "DCC"
			elif int(strN[-3]) == 6:
				buff = "DC"
			elif int(strN[-3]) == 5:
				buff = "D"
			elif int(strN[-3]) == 4:
				buff = "CD"
			else:
				for i in range(int(strN[-3])):
					buff += "C"

			numeral = buff + numeral

			if len(strN) > 3:
				for i in range(int(strN[:-3])):
					numeral = "M" + numeral



	return numeral


f = open("roman.txt", 'r')

numeralArray = f.read().split('\n')

tempLen = 0
savedSum = 0
for n in numeralArray:
	tempLen = len(n)
	diff = tempLen - len(printRome(calcRome(n)))

	if diff:
		savedSum += diff

print(savedSum)






