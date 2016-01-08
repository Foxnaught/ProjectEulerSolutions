
def fib(n):
	fib1 = 1
	fib2 = 1
	for i in range(3, n+1):
		test = fib1
		fib1 = fib2
		fib2 = test

		fib2 += fib1

	return fib2


fib1 = 1
fib2 = 1
pfib1 = 1
pfib2 = 1

k = 2
k2 = 2
numList = ['1','2','3','4','5','6','7','8','9']
fail = False
while 1:
	#fib1 = fib1 ^ fib2
	#fib2 = fib1 ^ fib2
	#fib1 = fib1 ^ fib2

	#This calculates the last 9 digits of the fibonacci sequence for efficiency
	#When a sequence of 1-9 is found it is passed to the progressive fibonacci loop
	temp = pfib1
	pfib1 = pfib2
	pfib2 = temp

	pfib2 += pfib1
	k += 1
	
	last9 = str(pfib2)[-9:]
	pfib2 = int(last9)

	fail = False
	for i in numList:
		if last9.count(i) != 1:
			fail = True
			break

	if not fail:
		#progressively proceed through the fibonacci sequence each time 1-9 is found on the last 9 digits
		#this prevents us from running over the same values when we get higher in the sequence
		while k2 < k:
			temp = fib1
			fib1 = fib2
			fib2 = temp

			fib2 += fib1
			k2 += 1

		print(k)
		first9 = str(fib2)[:9]
		fail = False
		for i in numList:
			if first9.count(i) != 1:
				fail = True
				break

		if not fail:
			print("\n" + str(k))
			break

	






