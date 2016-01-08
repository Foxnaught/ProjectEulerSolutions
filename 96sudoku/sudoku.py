from copy import deepcopy

def checkBoxes(grid):
	global standard

	for y in range(3):
		for x in range(3):
			tempBox = []
			for yMod in range(3):
				for xMod in range(3):
					tempBox.append(grid[y*3 + yMod][x*3 + xMod])

			if standard != sorted(tempBox):
				return False

	return True

def checkRows(grid):
	global standard

	for y in range(9):
		tempRow = []
		for i in range(9):
			tempRow.append(grid[y][i])

		if standard != sorted(tempRow):
			return False

	for x in range(9):
		tempRow = []
		for i in range(9):
			tempRow.append(grid[i][x])

		if standard != sorted(tempRow):
			return False

	return True

def getBoxMoves(grid, x, y):
	global standard

	tempBox = []
	for yMod in range(3):
		for xMod in range(3):
			tempBox.append(grid[int(y/3) * 3 + yMod][int(x/3) * 3 + xMod])

	options = []
	for s in standard:
		if s not in tempBox:
			options.append(s)

	return options

def getRowMoves(grid, x, y):
	global standard

	tempRow = []
	for i in range(9):
		tempRow.append(grid[y][i])
		tempRow.append(grid[i][x])

	options = []
	for s in standard:
		if s not in tempRow:
			options.append(s)

	return options

def isDone(grid):
	for i in grid:
		for t in i:
			if t == '0':
				return False

	return True

def getOptions(grid, x, y):
	options = []
	for result in getBoxMoves(grid, x, y):
		if result in getRowMoves(grid, x, y):
			options.append(result)

	return options


def validate(grid):
	if checkBoxes(grid) and checkRows(grid):
		return True
	else:
		return False


def checkMoves(argGrid, level=0):
	leastLoc = []
	leastOptions = []
	for y in range(9):
		for x in range(9):
			if argGrid[y][x] == '0':
				options = getOptions(argGrid, x, y)
				if len(options) == 0:
					return False

				if len(options) < len(leastOptions) or len(leastOptions) == 0:
					leastOptions = options
					leastLoc = [x, y]

				

	for result in leastOptions:
		tempGrid = deepcopy(argGrid)
		tempGrid[leastLoc[1]][leastLoc[0]] = result

		if not isDone(tempGrid):
			newGrid = checkMoves(tempGrid, level + 1)

			if newGrid != False:
				return newGrid
		elif validate(tempGrid):
			return tempGrid


	return False


def doObvious(newGrid):
	tempGrid = deepcopy(newGrid)
	for y in range(9):
		for x in range(9):
			if tempGrid[y][x] == '0':
				options = getOptions(tempGrid, x, y)
				if len(options) == 1:
					tempGrid[y][x] = options[0]

	return tempGrid


standard = ['1','2','3','4','5','6','7','8','9']



f = open('sudoku.txt', 'r')
line = f.readline().replace("\n", "")
grid = []
tSum = 0
count = 0
while(line):
	count += 1
	print(count)
	grid = []
	for i in range(9):
		line = f.readline().replace("\n", "")
		grid.append(list(line))

	line = f.readline()



	newGrid = deepcopy(grid)
	oldGrid = []
	while(newGrid != oldGrid):
		oldGrid = deepcopy(newGrid)
		newGrid = doObvious(oldGrid)

	grid = newGrid

	if not isDone(grid):
		grid = checkMoves(grid)

	tSum += int(grid[0][0] + grid[0][1] + grid[0][2])

	for i in grid:
		print(i)


print(tSum)