import math, time


def reverseStr(strN):
	newN = ""

	while strN != "":
		newN += strN[-1]
		strN = strN[:-1]

	return newN




n = 1000000000
#n = 1000000
#n = 1000
count = 0
start = time.time()
for i in reversed(range(n)):
	if not i % 100000:
		print(i)

	strI = str(i)

	first = int(strI[0])
	last = i % 10
	if last != 0 and last > first and (first + last) % 2:
		reverseInt = int(reverseStr(strI))
		
		strSum = str(i + reverseInt)

		found = True
		for char in strSum:
			if char in ['0', '2', '4', '6', '8']:
				found = False
				break

		if found:
			count += 1


print(count*2)
print("Time: " + str(time.time() - start))


