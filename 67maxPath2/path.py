def recursive(listArg, curPath=[], depth=0, ind=0):
	global triCost
	sumArray = []
	index = ind
	
	path = curPath[:] + [listArg[depth][index]]
	curSum = sumList(path)
	path1 = path2 = path

	if(len(listArg) - 1 > depth):
		if(curSum + listArg[depth+1][index] >= triCost[depth+1][index]):
			triCost[depth+1][index] = curSum + listArg[depth+1][index]
			path1 = recursive(listArg, path, depth+1, index)
		if(curSum + listArg[depth+1][index+1] >= triCost[depth+1][index+1]):
			triCost[depth+1][index+1] = curSum + listArg[depth+1][index+1]
			path2 = recursive(listArg, path, depth+1, index+1)
			
	
	if sumList(path2) > sumList(path1):
		path1 = path2

	return path1

def sumList(listArg):
	tSum = 0
	for l in listArg:
		tSum += l

	return tSum

f = open('triangle.txt')
line = f.readline()
tri = []
triCost = []
while(line):
	tempLine = []
	costLine = []
	for l in line.replace("\n", "").split(" "):
		tempLine.append(int(l))
		costLine.append(0)
	tri.append(tempLine)
	triCost.append(costLine)

	line = f.readline()

f.close()

test = recursive(tri)
print(test)

totalSum = 0
for t in test:
	totalSum += t

print(totalSum)