


def gcd(a, b):
	while b != 0:
		temp = b
		b = a % b
		a = temp

	return a


n = 24

print(n%8)
print(gcd(n, n/8))

unitaryDivisors = []
for i in range(1, n):
	if n % i == 0 and gcd(n, int(n/i)) == 1:
		unitaryDivisors.append(i)



uSum = 0
for i in unitaryDivisors:
	uSum += i*i


print(uSum)