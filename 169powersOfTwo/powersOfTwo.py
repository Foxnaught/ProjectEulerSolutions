import math
import time
import cProfile

def checkItems(listArg1, listArg2):
	#Make localized variables so we don't affect the lists outside the function
	list1 = listArg1
	list2 = listArg2[:]
	n = len(list1)
	n2 = len(list2)
	
	#We are going to loop though each item in the first list and compare it to each item in the second
	found = False
	foundIndex = 0
	counter = 0
	#If the shallowest level of the lists doesn't match in length then there is no way they are equivalent
	if n == n2:
		#Loop through list1 and try to match its elements to elements in lists 2
		#If the number of matched elemetns is equal to the length of list1, then they are equal.
		
		#The behavior of the function is difficult to describe when it encounters elements of a list that are also lists.
		#It recursively calls itself on the element and an element from the other list.
		#If those subsequent lists are simple (no list elements), they are compared normally and the result is added (or not) to the counter of the parent function call.
		#If they are not simple, the process starts again.
		for item1 in list1:
			found = False
			foundIndex = 0
			#To prevent counting the same items again, after an element in list2 is found to match,
			#the index of the matching element is removed from list2 for the next item1 in list1 to be compared
			for iter, item2 in enumerate(list2):
				
				#If both values are integers then compare them
				if type(item1) == int:
					#Make sure the second value is an integer otherwise they do not match
					if type(item2) == int:
						if item1 == item2:
							found = True
							#make sure we save where we are so we don't count this again
							foundIndex = iter
							#prematurely end the loop
							break
							
				#If both values are lists, compare them through recursion
				else:
					#We already know item1 is a list, if this one isn't then it won't match
					#if it is a list then we must compare the lists
					if type(item2) != int:
						#This is a direct comparison
						if item1 == item2:
							found = True
							foundIndex = iter
							break
						#This recurses to deeper levels of the lists to ensure they are not duplicates
						elif checkItems(item1, item2):
							
							found = True
							#make sure we save where we are se we don't count this again
							foundIndex = iter
							#prematurely end the loop
							break
				#Keep track of what iteration we are on
				
				
				
			#If we found a match for a value in list 1, incremenet our counter
			if found:
				counter += 1
				#We pop the value from the second list so it is not counted twice when we loop through it again
				list2.pop(foundIndex)
	
	#If the count of the resistors in both lists is equal then return true
	return (counter == n)

def newPow(n,a):
	temp = 1
	for i in range(a):
		temp = temp*n

	return temp

#base of 2 is assumed
#Numbers are 2 to an exponent value
def combos(exp):
	sumList = [[exp]]

	for e in range(1, exp+1):
		sumList.append(sumList[-1][:-1] + [exp-e] + [exp-e])

	return sumList

def maxBinarySum(n):
	sumList = []
	maxExp = int(math.log(n)/math.log(2))
	sumList.append(maxExp)
	if(n-newPow(2, maxExp) > 0):
		sumList.extend(maxBinarySum(n-newPow(2, maxExp)))


	return sumList

def combineLists(list1, list2):
	totalList = []
	for i in list1:
		for t in list2:
			totalList.append([i + t])

def checkCount(listArg):
	listLen = len(listArg)
	count = 0
	for i in range(listLen):
		count = 0
		for t in range(listLen):
			if listArg[i] == listArg[t]:
				count += 1
				if(count > 2):
					return False

	return True



def degenerate(sumList):
	found = False

	degenList = []
	for i in range(len(sumList)):
		key = sumList[i]
		if key != 0:
			tempDegen = sorted(sumList[:i] + sumList[i+1:] + [key-1]*2)
			if tempDegen not in degenList:
				found = False
				for t in sumList:
					if key-1 == t:
						found = True
						break

				if(not found):
					degenList.extend(degenerate(tempDegen))
					degenList.append(tempDegen)

	return degenList



def testCheck(list1, listLen):
	i = 0

	while i < listLen-2:
		if list1[i] == list1[i+1] == list1[i+2]:
			return False
		elif list1[i+1] != list1[i+2]:
			i += 2
		else:
			i += 1

	return True

def testCheck2(list1, list2):
	count = 0

	for i in range(len(list1)):
		count = 0
		for t in range(len(list2)):
			if list1[i] == list2[t]:
				count += 1

				if count > 1:
					return False

	return True		


def tryDegen():
	degen = degenerate(sumArray)
	degen.append(sumArray)
	dupeList = []
	dupeCount = 0
	for i in degen:
		if sorted(i) not in dupeList:
			print(i)
			dupeList.append(sorted(i))
		else:
			dupeCount += 1

	print(len(degen) - dupeCount)
	quit()

def main():
	sumArray = maxBinarySum(newPow(10, 9))
	#sumArray = maxBinarySum(10)

	totalComboArray = combos(sumArray.pop(0))
	#quit()


	newTotalComboArray = []
	badComboArray = []
	#print(totalComboArray)
	#quit()
	print(sumArray)
	sumList = []
	startTime = time.time()
	accepted = False
	for i in sumArray:
		print(i)
		print(len(totalComboArray))

		sumList = [[i]] + [[0]]*i
		for e in range(i+1):
			if(e > 0):
				sumList[e] = sumList[e-1][:-1] + [i-e]*2


			c = sumList[e]
			cLen = e+1


			for t in totalComboArray:
				combine = sorted(t+c)

				if (testCheck(combine, len(t) + cLen) and combine not in newTotalComboArray):
					newTotalComboArray.append(combine)
					

		totalComboArray = newTotalComboArray

		newTotalComboArray = []

	endTime = time.time() - startTime
	print(len(totalComboArray))
	print(endTime)

	quit()

	print("----")
	print(len(newComboArray))

#cProfile.run('main()')
main()