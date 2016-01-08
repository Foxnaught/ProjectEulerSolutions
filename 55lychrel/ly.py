import math

def isPalindrome(text):
	for i in range(math.floor(text.__len__()/2)):
		if text[i] != text[text.__len__()-i-1]:
			return False

	return True

def checkLychrel(number):
	for i in range(50):
		revNum = list(str(number))
		revNum.reverse()
		number += int(''.join(revNum))

		if isPalindrome(str(number)):
			return False

	return True


count = 0
for i in range(10000):
	if checkLychrel(i):
		count += 1

print(count)



