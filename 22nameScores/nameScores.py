def findLetterScore(letter, alphabet):
	for a in range(len(alphabet)):
		if letter == alphabet[a]:
			return (a+1)

alphabet = []
for i in list(range(97, 123)):
	alphabet.append(chr(i))


f = open('names.txt', 'r')
text = sorted(f.read().replace('\"', "").lower().split(','))


totalScore = 0
for word in range(len(text)):
	letterScore = 0
	for letter in text[word]:
		letterScore += findLetterScore(letter, alphabet)

	totalScore += letterScore * (word+1)

print(totalScore)