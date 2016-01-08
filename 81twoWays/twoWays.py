from copy import deepcopy

#Recursively set the cost to move to any position on the grid
#Stops if the next step costs more than previous attempts
#or if the last step costs less
def recursive(grid, curPath=[], depth=0, index=0):
	global gridCost
	curPath += [grid[depth][index]]
	curSum = sumList(curPath)

	if curSum < gridCost[-1][-1] or gridCost[-1][-1] == 0:
		if(index+1 < len(grid[depth]) and (0 == gridCost[depth][index+1] or gridCost[depth][index+1] > curSum + grid[depth][index+1])):
			gridCost[depth][index+1] = curSum + grid[depth][index+1]
			recursive(grid, deepcopy(curPath), depth, index+1)

		if(depth+1 < len(grid) and (0 == gridCost[depth+1][index] or gridCost[depth+1][index] > curSum + grid[depth+1][index])):
			gridCost[depth+1][index] = curSum + grid[depth+1][index]
			recursive(grid, deepcopy(curPath), depth+1, index)

def sumList(listArg):
	lSum = 0
	for i in listArg:
		lSum += i

	return lSum

def checkIfLowest(gridCost, depth, index, value):
	for i in range(depth+index):
		t = depth + index - i - 1
		if value > gridCost[t][i] and gridCost[t][i] != 0:
			return False

	return True

f = open("matrix.txt", 'r')

text = f.readline().replace("\n", "")
matrixArray = []
matrixCost = []

#Size of grid
#Allows limiting of larger grids
nXn = int(len(text.split(",")))

count = 0
while count < nXn:
	count += 1
	matrixCost.append([0] * len(text.split(",")[:nXn]))
	matrixArray.append(text.split(",")[:nXn])
	text = f.readline().replace("\n", "")

for i in range(len(matrixArray)):
	for t in range(len(matrixArray[0])):
		matrixArray[i][t] = int(matrixArray[i][t])

for m in matrixArray:
	print(m)

index = 0


gridCost = matrixCost
bestPath = recursive(matrixArray)
for m in gridCost:
	print(m)


print(matrixCost[-1][-1])


