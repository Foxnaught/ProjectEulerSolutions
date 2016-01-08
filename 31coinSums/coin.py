import time


def subDivide(nList, mainLine=[]):
	retLists = [nList]
	checkedValues = []
	for n in range(len(nList)):
		if nList[n] > 1 and nList[n] not in checkedValues:
			checkedValues.append(nList[n])

			temp = nList[:n] + nList[n+1:]

			if nList[n] == 200:
				temp.extend([100, 100])
			elif nList[n] == 100:
				temp.extend([50, 50])
			elif nList[n] == 50:
				#Normally we would break 50 into 20 20 and 10
				#However if there is already a 10 in the list and since we are breaking down maximum values
				#We need to combine these tens or else we are leaving out a critical solution (maximum value)
				#Example the next maximum value for 10 20 20 50 is 20 20 20 20 20 not 10 20 20 10 20 20
				#If you don't combine the 10's then you are skipping a maximum value
				if 10 in temp:
					del temp[temp.index(10)]

					temp.extend([20, 20, 20])
				else:
					temp.extend([20, 20, 10])
			elif nList[n] == 20:
				temp.extend([10, 10])
			elif nList[n] == 10:
				temp.extend([5,5])
			elif nList[n] == 5:
				#This is the same fix as the one above but for 1's and 2's instead of 10's and 20's
				if 1 in temp:
					del temp[temp.index(1)]

					temp.extend([2, 2, 2])
				else:
					temp.extend([2,2,1])
			elif nList[n] == 2:
				temp.extend([1,1])

			temp = sorted(temp)

			if temp not in mainLine + retLists:
				retLists.extend(subDivide(temp, mainLine + retLists))

	return retLists


temp = []
total = subDivide([200])
for i in total:
	if sorted(i) not in temp:
		temp.append(sorted(i))

print(len(temp))


retLists = []



