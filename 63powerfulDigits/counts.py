

def pow(a, b):
	ret = 1
	for i in range(b):
		ret = ret * a

	return ret

def limit(nDigits):
	limit = 9
	for i in range(nDigits-1):
		limit = int(str(limit) + "9")

	return limit

sPow = 1
sNum = 1
count = 0;
for i in range(1, 101):
	for n in range(1, 2000):
		if(len(str(pow(n,i))) == i):
			print(i)
			count += 1

print("\n" + str(count))

