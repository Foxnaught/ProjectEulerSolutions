

lowestI = 0
for i in range(1, 10000000):
	sortedList = sorted(str(i))
	isPermute = True
	for m in range(2, 7):
		tempList = sorted(str(i*m))
		if len(tempList) != len(sortedList) or tempList != sortedList:
			isPermute = False

	if isPermute:
		print(i)
		quit()




