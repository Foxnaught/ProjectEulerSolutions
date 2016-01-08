import time

def checkRoyalFlush(hand):
	global royalList

	for card in royalList:
		if card not in hand:
			return False

	return True

def checkFlush(hand):
	suit = hand[0][1]

	for i in hand[1:]:
		if i[1] != suit:
			return False

	return True

def checkFour(hand):
	for i in hand:
		if countInHand(hand, i[0]) == 4:
			return True

	return False

def checkThree(hand):
	for i in hand:
		if countInHand(hand, i[0]) == 3:
			return True

	return False

def countInHand(hand, val):
	count = 0
	for i in hand:
		if i[0] == val:
			count += 1

	return count

def numOfPairs(hand):
	foundList = []
	for i in hand:
		if countInHand(hand, i[0]) == 2 and i[0] not in foundList:
			foundList.append(i[0])

	return len(foundList)

def checkStraight(hand):
	smallest = rateCard(hand[0][0])
	for i in hand[1:]:
		next = rateCard(i[0])
		if next < smallest:
			smallest = rateCard(i[0])
		elif next == smallest:
			return False

	for i in range(4):
		found = False
		for i in hand:
			if smallest + 1 == 14:
				if i[0] == 'A':
					found = True
					break
			if rateCard(i[0]) == smallest + 1:
				smallest = rateCard(i[0])
				found = True
				break

		if not found:
			return False

	return True

def pullHighest(hand):
	highIndex = 0
	high = rateCard(hand[0][0])
	if not high:
		del hand[0]
		return 14

	for i in range(1, len(hand)):
		if rateCard(hand[i][0]) > high or not rateCard(hand[i][0]):
			high = rateCard(hand[i][0])
			highIndex = i
			if not high:
				del hand[i]
				return 14

	del hand[highIndex]
	return high

def getHighFour(hand):
	for i in hand:
		if countInHand(hand, i[0]) == 4:
			return rateCard(i[0])

def getHighThree(hand):
	for i in hand:
		if countInHand(hand, i[0]) == 3:
			return rateCard(i[0])

def getHighPair(hand, exclude = -1):
	high = -1
	for i in hand:
		if countInHand(hand, i[0]) == 2 and (rateCard(i[0]) > high or not rateCard(i[0]) or high == -1):
			if not rateCard(i[0]) and exclude != 14:
				return 14

			if rateCard(i[0]) != exclude:
				high = rateCard(i[0])

	return high

def rateHand(hand):
	if checkRoyalFlush(hand):
		return 9
	elif checkStraight(hand) and checkFlush(hand):
		return 8
	elif checkFour(hand):
		return 7
	elif checkThree(hand) and numOfPairs(hand):
		return 6
	elif checkFlush(hand):
		return 5
	elif checkStraight(hand):
		return 4
	elif checkThree(hand):
		return 3
	elif numOfPairs(hand) == 2:
		return 2
	elif numOfPairs(hand) == 1:
		return 1
	else:
		return 0

def rateCard(card):
	global cardList

	return cardList.index(card)


royalList = ['A', 'K', 'Q', 'J', '10']
cardList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']


f = open("poker.txt", "r")
line = f.readline().replace("\n", "")
hand1Wins = 0
oldWins = 0
losses = 0
while line:
	hand1 = line.split(" ")[:5]
	hand2 = line.split(" ")[5:]
	print(hand1)
	print(hand2)

	rating1 = rateHand(hand1)
	rating2 = rateHand(hand2)
	done = False

	if rating1 > rating2:
		hand1Wins += 1
	elif rating1 == rating2:
		if rating1 == 1:
			high1 = getHighPair(hand1)
			high2 = getHighPair(hand2)
			print(high1)
			print(high2)
			if high1 > high2:
				hand1Wins += 1
				done = True
			elif high1 < high2:
				done = True
		elif rating1 == 2:
			high1 = getHighPair(hand1)
			high2 = getHighPair(hand2)

			if high1 > high2:
				hand1Wins += 1
				done = True
			elif high1 < high2:
				done = True

			if not done:
				high1 = getHighPair(hand1, high1)
				high2 = getHighPair(hand2, high2)

				if high1 > high2:
					hand1Wins += 1
					done = True
				elif high1 < high2:
					done = True

		elif rating1 == 3:
			high1 = getHighThree(hand1)
			high2 = getHighThree(hand2)

			if high1 > high2:
				hand1Wins += 1
				done = True
			elif high1 < high2:
				done = True

		elif rating1 == 4 or rating1 == 5 or rating1 == 8:
			high1 = pullHighest(hand1)
			high2 = pullHighest(hand2)

			if high1 > high2:
				hand1Wins += 1
				done = True
			elif high1 < high2:
				done = True

		elif rating1 == 6:
			high1 = getHighThree(hand1)
			high2 = getHighThree(hand2)

			if high1 > high2:
				hand1Wins += 1
				done = True
			elif high1 < high2:
				done = True

			if not done:
				high1 = getHighPair(high1)
				high2 = getHighPair(high2)

				if high1 > high2:
					hand1Wins += 1
					done = True
				elif high1 < high2:
					done = True

		elif rating1 == 7:
			high1 = getHighFour(hand1)
			high2 = getHighFour(hand2)

			if high1 > high2:
				hand1Wins += 1
				done = True
			elif high1 < high2:
				done = True


		if not done:
			while 1:
				high1 = pullHighest(hand1)
				high2 = pullHighest(hand2)

				if high1 > high2:
					hand1Wins += 1
					break
				elif high2 > high1:
					break

	line = f.readline().replace("\n", "")

	if hand1Wins != oldWins:
		print("Win!")
		oldWins = hand1Wins

	else:
		print("Lose!")
		losses += 1


print(hand1Wins)










