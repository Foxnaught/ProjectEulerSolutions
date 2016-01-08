import math

def exp(a,b):
	p = 1
	for i in range(b):
		p = p * a

	return p

tSum = 0
for n in range(1, 1001):
	tSum += int(exp(n,n))

print(str(tSum)[-10:])

