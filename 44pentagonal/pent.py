import math

def getPent(n):
	return (n * (3 * n - 1))/2

def isPent(n):
	temp = getIndex(n)

	return int(temp) == temp

def getIndex(n):
	return (math.sqrt(24 * n + 1) + 1)/6


smallestP2 = 1
p1 = 2
prevP1Val = 1

found = False
while not found:
	p1Val = getPent(p1)

	for p2 in range(1, p1):
		p2Val = getPent(p2)
		
		#IF p1 and p2 make p3		
		if isPent(p1Val + p2Val):
			#smallestP2 = p2Val

			#And p1 and p3 make p4
			#Then that means p3 - p1 = p2
			#p2 is the valid difference
			if isPent(p1Val - p2Val):
				found = True
				print("Success")
				print(p1Val - p2Val)
				break

	p1 += 1
	prevP1Val = p1Val


