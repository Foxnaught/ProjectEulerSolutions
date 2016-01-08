import math

def isPalindrome(text):
	for i in range(math.floor(text.__len__()/2)):
		if text[i] != text[text.__len__()-i-1]:
			return False

	return True

def toBinary(num):
	newNum = num
	binary = ""
	while 1:
		if newNum % 2:
			binary += '1'
		else:
			binary += '0'

		if newNum == 1:
			break
		else:
			newNum = int(math.floor(newNum/2))

	return binary


tSum = 0
for n in range(1, 1000000):
	if isPalindrome(str(n)):
		if isPalindrome(toBinary(n)):
			print(n)
			tSum += n

print()
print(tSum)