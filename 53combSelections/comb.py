

def fact(n):
	mult = 1
	for i in range(2, n+1):
		mult = mult * i

	return mult

def combine(n, r):
	return fact(n)/(fact(r)*(fact(n-r)))



count = 0
for n in range(101):
	for r in range(n):
		if combine(n, r) > 1000000:
			count += 1

print(count)

