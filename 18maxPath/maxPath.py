def recursive(listArg, ind=0):
	temp = 0

	sumArray = []
	tempList = listArg
	index = ind
	
	
	sum1 = int(tempList[0][index])
	sum2 = sum1

	if(len(listArg) > 1):
		newList = []
		for t in tempList[1:]:
			newList.append(t[:])

		sum1 += recursive(newList[:], index)
		sum2 += recursive(newList[:], index+1)

	
	if sum2 > sum1:
		sum1 = sum2



	return sum1

f = open("triangle.txt")

triangleArray = []
text = f.readline()
while text.__len__() > 0:
	triangleArray.append(text.replace("\n", "").split(" "))
	text = f.readline()

print(recursive(triangleArray))