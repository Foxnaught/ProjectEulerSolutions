import math



smallestDiff = 20000000


#width
m = 0
#length
n = 0

counting = True
rSum = 0
smallSum = 0
smallArea = 0
quitLoop = False

while m < 2000:
	m += 1
	print(m)
	for n in range(1, m+1):
		tempDiff = 2000000
		rSum = 0
		for a in range(m):
			for b in range(n):
				rSum += (m - a) * (n - b)

				if math.fabs(2000000 - rSum) < tempDiff:
					tempDiff = math.fabs(2000000 - rSum)
					shrinking = True
				elif shrinking:
					shrinking = False
					quitLoop = True
					break

			if quitLoop:
				quitLoop = False
				break

		if math.fabs(2000000 - rSum) < smallestDiff:
			smallestDiff = math.fabs(2000000 - rSum)
			smallSum = rSum
			smallArea = n * m
			print(smallestDiff)

print(smallSum)
print(smallArea)