import math

def generateSpiral(n):
	grid = [0]*n
	for i in range(n):
		grid[i] = [0]*n

	centerX = int((n-1)/2)
	centerY = centerX

	leftX, rightX, topY, botY = 0,0,0,0
	direction = 0
	x = 0
	y = 0

	curNum = 0
	while(1):
		if curNum == n*n:
			break

		if grid[centerY + y][centerX + x] == 0 or (x == -1 and y == -2):
			curNum += 1
			grid[centerY + y][centerX + x] = curNum

		
		if direction == 0:
			if x > rightX or x + centerX == n - 1:
				direction = 1
				rightX = x
			else:
				x += 1
				

		if direction == 1:
			if y > topY or y + centerY == n - 1:
				direction = 2
				topY = y
			else:
				y += 1
				

		if direction == 2:
			if x < leftX or x + centerX == 0:
				direction = 3
				leftX = x
			else:
				x -= 1
				

		if direction == 3:
			if y < botY or y + centerY == 0:
				direction = 0
				botY = y
			else:
				y -= 1


	return grid

xMod = 0
yMod = 0
crossSum = 0
for i in generateSpiral(1001):
	if xMod != len(i) - yMod - 1:
		crossSum += i[xMod] + i[len(i)-yMod-1]
	else:
		crossSum += i[xMod]

	xMod += 1
	yMod += 1

print(crossSum)
