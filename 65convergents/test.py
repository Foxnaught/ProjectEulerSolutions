

def getConvergent(n):
	cSum = 0
	num = 0
	denom = 1
	k = int(n/3)
	for i in range(0,n):
		t = n - i

		if cSum:
			cSum = 1/cSum
			denom = num ^ denom
			num = num ^ denom
			denom = num ^ denom

		if not t % 3:
			cSum += 2*k
			num += 2*k*denom
			k -= 1
		elif t == 1:
			cSum += 2
			num += 2*denom
		else:
			cSum += 1
			num += denom

	return num


c = getConvergent(100)

cSum = 0
for i in str(c):
	cSum += int(i)

print(cSum)


