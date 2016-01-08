#fib(1) == 1
#fib(2) == 1
#fib(3) == 2
#fib(4) == 3
#fib(5) == 5
def fib(n):
	fibVal = 1
	oldVal = 1
	secondOld = 0

	for i in range(n-1):
		fibVal = oldVal + secondOld
		secondOld = oldVal
		oldVal = fibVal

	return fibVal

index = 0
tFib = ""
while 1:
	sFib = fib(index)
	sFib = str(sFib)
	if(sFib.__len__() == 1000):
		print(index)
		tFib = sFib
		break
	else:
		index += 1

print(tFib)






