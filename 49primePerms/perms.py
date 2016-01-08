import math

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

#must be same length
def isPan(base, test):
	for i in base:
		if i not in test:
			return False

	return True

def hasRepeats(test):
	for i in test:
		if test.count(i) > 1:
			return True

	return False

def SOE(n):
	numList = list(range(n))
	primes = [2]
	for i in range(3, n, 2):
		if numList[i]:
			primes.append(i)

			mult = 3
			while i * mult < n:
				numList[i*mult] = 0
				mult += 2

	return primes


#Start from the example
n1 = 1487
#n1 = 0
searching = True

str1 = ""
str2 = ""
str3 = ""

primes = SOE(10000)
while searching and n1 != 9999:
	n1 += 1
	str1 = str(n1)
	newStr = str1[:]
	if int(str1) in primes:
		while 1:
			list2 = nextPan(newStr)

			if list2:
				str2 = ''.join(list2)
				if int(str2) in primes:
					str3 = str(2*int(str2) - n1)
					if len(str1) == len(str3) and isPan(str1, str3):
						if int(str3) in primes:
							searching = False
							print("found")
							print(n1)
							print(int(str2))
							print(int(str3))
							print(str(n1) + str2 + str3)
							break

				newStr = str2[:]
			else:
				break

	



