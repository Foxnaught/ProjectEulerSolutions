import math

maxP = 0
maxList = []
maxLen = len(maxList)
for p in range(12, 1001):
	print(p)
	combos = []
	cLen = 0
	for a in range(1, p):
		for b in range(1, p-a):
			root = math.sqrt(a*a+b*b)
			intRoot = int(root)
			if (root - intRoot) == 0.0 and a + b + intRoot == p:
				combos.append((a,b,root))
				cLen += 1

	if cLen > maxLen:
		maxP = p
		maxList = combos
		maxLen = len(maxList)

print(maxP)
print(maxList)