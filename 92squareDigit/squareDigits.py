def squareSum(value):
	squareSum = 0

	for i in str(value):
		i = int(i)
		squareSum += i*i

	return squareSum



tempValue = 0
digitArray = []
valueArray = []
unitArray = []
maxRange = int(input("Set max range: "))

#The square sum for a large number is significantly smaller than the original number
#We will account for all chains below the maximum squareSum of the range
#This makes it so that when we loop over it over large ranges, the interval between loops is consistent and doesn't increase with i
#Otherwise we would be adding values higher than the maximum square sum and wasting resources each loops past that
for i in range(1, squareSum(maxRange-1)):
	if i not in unitArray:
		chainArray = []
		tempValue = i
		chainArray.append(tempValue)
		while(True):
			tempValue = squareSum(tempValue)
			chainArray.append(tempValue)

			if(tempValue in digitArray or tempValue == 89):
				digitArray.extend(chainArray)
				break
			if(tempValue in unitArray or tempValue == 1):
				unitArray.extend(chainArray)
				break

for i in range(1, maxRange):
	if(i % 100000 == 0):
		print(i)

	#If the value we are checking for isn't already determined to go to one then check it
	tempValue = i
	while(tempValue not in unitArray):
		#print(unitArray)
		tempValue = squareSum(tempValue)

		#If the square sum falls in the array that holds values that go to zero then extend it by the square sums in the chain
		if(tempValue in digitArray or tempValue == 89):
			valueArray.append(i)
			break

print(len(valueArray))