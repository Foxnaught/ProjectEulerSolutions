

def getConvergent(n):
	cSum = 0
	num = 0
	denom = 1
	k = int(n/3)
	for i in range(n):
		t = n - i

		if cSum:
			cSum = 1/cSum
			denom = num ^ denom
			num = num ^ denom
			denom = num ^ denom
		
		if t == 1:
			cSum += 1
			num += denom
		else:
			cSum += 1
			num += 2*denom

	return [num, denom]


n = 1
result = [1, 1]

count = 0
while n < 999:
	result = getConvergent(n+1)
	if len(str(result[0])) > len(str(result[1])):
		count += 1

	n += 1

print(count)