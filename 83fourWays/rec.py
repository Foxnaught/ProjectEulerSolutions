

def recurseSearch(pos, travelCost, chain=[]):
	global matrix
	global costMatrix
	global mLen


	if travelCost < costMatrix[mLen-1][mLen-1] or not costMatrix[mLen-1][mLen-1]:
		#right
		if pos[0] != mLen - 1 and [pos[0]+1,pos[1]] not in chain:
			right = matrix[pos[0]+1][pos[1]]
			if costMatrix[pos[0]+1][pos[1]] == 0 or costMatrix[pos[0]+1][pos[1]] > travelCost + right:
				costMatrix[pos[0]+1][pos[1]] = travelCost + right
				if [pos[0]+1, pos[1]] != [mLen-1, mLen-1]:
					recurseSearch([pos[0]+1, pos[1]], travelCost + right, chain + [right])
				else:
					print(costMatrix[mLen-1][mLen-1])
		#down
		if pos[1] != mLen - 1 and [pos[0], pos[1]+1] not in chain:
			down = matrix[pos[0]][pos[1]+1]
			if costMatrix[pos[0]][pos[1]+1] == 0 or costMatrix[pos[0]][pos[1]+1] > travelCost + down:
				costMatrix[pos[0]][pos[1]+1] = travelCost + down
				if [pos[0], pos[1]+1] != [mLen-1, mLen-1]:
					recurseSearch([pos[0], pos[1]+1], travelCost + down, chain + [down])
				else:
					print(costMatrix[mLen-1][mLen-1])

		#left
		if pos[0] != 0 and [pos[0]-1, pos[1]] not in chain:
			left = matrix[pos[0]-1][pos[1]]
			if costMatrix[pos[0]-1][pos[1]] == 0 or costMatrix[pos[0]-1][pos[1]] > travelCost + left:
				costMatrix[pos[0]-1][pos[1]] = travelCost + left
				if [pos[0]-1, pos[1]] != [mLen-1, mLen-1]:
					recurseSearch([pos[0]-1, pos[1]], travelCost + left, chain + [left])
				else:
					print(costMatrix[mLen-1][mLen-1])

		#up
		if pos[1] != 0 and [pos[0], pos[1]-1] not in chain:
			up = matrix[pos[0]][pos[1]-1]
			if costMatrix[pos[0]][pos[1]-1] == 0 or costMatrix[pos[0]][pos[1]-1] > travelCost + up:
				costMatrix[pos[0]][pos[1]-1] = travelCost + up
				if [pos[0], pos[1]-1] != [mLen-1, mLen-1]:
					recurseSearch([pos[0], pos[1]-1], travelCost + up, chain + [up])
				else:
					print(costMatrix[mLen-1][mLen-1])



matrixFile = open("matrix.txt", "r")
matrix = []

line = matrixFile.readline()
while(line):
	matrix.append(line.split(","))
	line = matrixFile.readline()

costMatrix = []
for i in range(len(matrix)):
	costMatrix.append([0]*len(matrix))
	for t in range(len(matrix[i])):
		matrix[i][t] = int(matrix[i][t])

mLen = len(matrix)
recurseSearch([0,0], matrix[0][0])
print(costMatrix[len(costMatrix)-1][len(costMatrix)-1])
