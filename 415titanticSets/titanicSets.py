from sympy.parsing.sympy_parser import parse_expr
import cProfile
import math
import time
import sys

def checkTitanic(titanicSet):
	#loop through and compare ever item with every other item
	#We will then calculate a line and see if it can be fitted to any other item in the set
	firstArray = []
	secondArray = []
	for i in titanicSet:
		for t in titanicSet:
			#The second clause prevents checking the same line in the opposite direction
			if i != t and (t not in firstArray or i not in secondArray):
				firstArray.append(i)
				secondArray.append(t)
				lineVector = (i[0]-t[0], i[1]-t[1])
				factor = findHighFactor(lineVector[0], lineVector[1])
				#Reduce the vectors to smallest integers.
				lineVector = (lineVector[0]/factor, lineVector[1]/factor)

				isTitan = True
				
				for final in titanicSet:
					yTest = True
					xTest = True
					if final != t != i:
						if(lineVector[0] == 0):
							if(i[0]-final[0] == 0):
								xTest = False
						elif(lineVector[0] == (i[0]-final[0]) % lineVector[0] == 1):
							xTest = False
						elif((i[0]-final[0]) % lineVector[0] == 0 and i[0] - final[0] != 0):
							xTest = False

						if(lineVector[1] == 0):
							if(i[1]-final[1] == 0):
								yTest = False
						elif(lineVector[1] == (i[1]-final[1]) % lineVector[1] == 1):
							yTest = False
						elif((i[1]-final[1]) % lineVector[1] == 0 and i[1] - final[1] != 0):
							yTest = False

						if(not yTest and not xTest):
							isTitan = False
							break


				if(isTitan):
					return True

	#If we didnt determine it is a titan set then return False
	return False


def newCheckTitanic(titanSet):
	global boxValue
	n = boxValue
	lineVectorArray = []

	for i in range(n):
		lineVectorArray.extend([[1, i],[i, 1]])

	
	for t in lineVectorArray:
		count = 0
		for i in range(1, n):
			if([t[0]*i, t[1]*i] in titanSet):
				count += 1
				if count > 2:
					break

		if count <= 2:
			return True

	return False



def grow(initSet):
	global boxValue
	n = boxValue
	setList = []
	firstArray = []
	secondArray = []

	for i in initSet:
		for t in initSet:
			#The first part prevents us from matching the same point
			#The second part prevents us from trying the same line backwards
			if i != t and (i not in secondArray or t not in firstArray):
				firstArray.append(i)
				secondArray.append(t)
				lineSet = [i, t]
				newSet = []

				lineVector = (i[0]-t[0], i[1]-t[1])
				factor = findHighFactor(lineVector[0], lineVector[1])
				#Reduce the vectors to smallest integers.
				lineVector = (lineVector[0]/factor, lineVector[1]/factor)
				setList.append(lineSet)

				

				for final in initSet:
					if t != final != i:
						xTest = True
						yTest = True

						if(lineVector[0] == 0):
							if(i[0]-final[0] == 0):
								xTest = False
						elif(lineVector[0] == (i[0]-final[0]) % lineVector[0]):
							xTest = False
						elif((i[0]-final[0]) % lineVector[0] == 0 and i[0] - final[0] != 0):
							xTest = False

						if(lineVector[1] == 0):
							if(i[1]-final[1] == 0):
								yTest = False
						elif(lineVector[1] == (i[1]-final[1]) % lineVector[1]):
							yTest = False
						elif((i[1]-final[1]) % lineVector[1] == 0 and i[1] - final[1] != 0):
							yTest = False

						if(yTest or xTest):
							#New set is where we put all valid extra point for the given lineset (two points)
							#Later we will pass new set into a function that obtains all permutations of all lengths of the set
							newSet.append(final)

				#This loops through all permutations of the set of extra points we made and concatenates them to the lineSet (the base two points)
				for perm in allListCombos(newSet):
					if(perm + lineSet not in setList):
						setList.append(perm + lineSet)
	return setList








def allListCombos(rList):
	comboList = [rList]
	tempList = []
	n = len(rList)

	if(n >= 3):
		for i in range(n):
			tempList = rList[:i] + rList[i+1:]

			comboList.extend(allListCombos(tempList))

	return comboList
						
def findHighFactor(number1, number2):
	if number1 < 0:
		number1 = number1 * -1
	if number2 < 0:
		number2 = number2 * -1


	maxNumber = number2
	if(number1 > number2):
		maxNumber = number1


	factor = 1
	for i in range(1, maxNumber+1):
		if(number1 % i == 0 and number2 % i == 0):
			factor = factor * i

	return factor

def compareLists(list1, list2):
	for i in list1:
		found = False
		tempList = []
		for t in list2:
			if i == t and not found:
				found = True
			else:
				tempList.append(t)

		if not found:
			return False
		#Reset list 2 without the value we matched
		list2 = tempList

	return True

def factorial(n):
	product = 1
	for i in range(2, n+1):
		product = product*i

	return product

def countOptions(n):
	count = 0
	for i in range(2, math.floor(n*n/2)+1):
		product = 1
		for b in range(i):
			product = product * (n*n-b)

		denom = str(factorial(i))[1000:]
		num = str(product)[1000:]

		try:
			int(denom)
			int(num)

			if(denom != '' and num != ''):
				denom = int(denom)
				count += int(str(product)[1000:])/(int(str(factorial(i))[1000:]))
		except:
			pass

		if(i%1000 == 0):
			print(i)

	count = count * 2

	if((n*n/2) % 2 == 1):
		count += int(str(factorial(n*n))[1000:])/int(str(factorial(math.floor(n*n/2)+1)*factorial(n*n - math.floor(n*n/2) - 1))[1000:])

	count += int(str((n*n) + 1)[1000:])

	return count


def main():
	n=int(input("squared value: "))
	global boxValue
	boxValue = n

	#Build a 2x2 box to grow from
	initSet = []
	for x in range(n+1):
		for y in range(n+1):
			initSet.append((x, y))


	tempSet = []
	comboList = []
	startTime = time.time()
	print(countOptions(n))
	endTime = time.time() - startTime
	

	print("Time to execute recursive function: " + str(endTime))

	quit()

	print("Original length " + str(len(comboList)))
	
	for combo in comboList:
		if len(combo) >= 2 and checkTitanic(combo) and combo not in tempSet:
			tempSet.append(combo)

	print(len(tempSet))
	
	deuce = []
	for i in tempSet:
		if len(i) == 2:
			print(i)
			deuce.append(i)

	print(len(deuce))
	finalSet = tempSet


	
	

	
	



#print(checkTitanic([[1,2],[3,3],[2,4]]))
boxValue = 0


main()

quit()
cProfile.run('main()')