


def getTriangle(n):
	return int((n*(n+1))/2)

def getWordSum(word):
	charList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	wordSum = 0
	for char in word:
		wordSum += charList.index(char) + 1

	return wordSum



f = open('words.txt', 'r')
text = f.read()
f.close()

words = text.replace("\"", "").lower().split(',')
triCount = 0
for w in words:
	wordSum = getWordSum(w)
	
	for i in range(wordSum+1):
		if wordSum == getTriangle(i):
			triCount += 1
			break


print(triCount)