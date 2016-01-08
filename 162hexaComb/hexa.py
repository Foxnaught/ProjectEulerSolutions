

def combine(nList):
	hexList = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	hexList = ['0','1','2']
	combList = []
	for n in nList:
		newList = nList[:]
		for t in hexList:
			if t not in newList:
				newList.append(t)

			if len(newList) > 0:
				combList.append(newList)
				combList.extend(combine(newList))

	return combList


for i in combine(['0','1','2']):
	print(i)