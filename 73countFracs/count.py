
def gcd(a, b):
	while b:
		a = a % b

		a = a ^ b
		b = a ^ b
		a = a ^ b

	return a

def primeFactors(n):
	factors = []
	count = 2
	while n != 1:
		if not n % count:
			n = n / count

			if count not in factors:
				factors.append(count)
		else:
			count += 1

	return factors


count = 0
fracList = []
for denom in reversed(range(1, 12001)):
	print(denom)
	for num in range(int(denom/3)+1, int(denom/2)+1):
		if num/denom > 1/3 and num/denom < 1/2:
			#gcDenom = gcd(denom, num)
			#num = int(num / gcDenom)
			#denom = int(denom / gcDenom)
			
			if(gcd(denom, num) == 1):
				count += 1


print(count)

