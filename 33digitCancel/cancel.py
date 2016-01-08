


def reduceTerms(f):
	newF = f
	for i in range(2, max(newF[0],newF[1])):
		if newF[0] % i == 0 and newF[1] % i == 0:
			newF[0] = int(newF[0]/i)
			newF[1] = int(newF[1]/i)
			newF = reduceTerms(newF)
			break

	return newF





fracList = []

for a in range(10, 100):
	for b in range(10, 100):
		stringA = str(a)
		stringB = str(b)

		if (stringB[0] != '0' and stringA[0] == stringB[1] and int(stringA[1])/int(stringB[0]) == a/b) or (stringB[1] != '0' and stringA[1] == stringB[0] and int(stringA[0])/int(stringB[1]) == a/b):
			if stringA[0] != stringB[0] and stringA[1] != stringB[1]:
				if sorted((a,b)) not in fracList:
					fracList.append(sorted([a,b]))

for f in fracList:
	print(f)

print(len(fracList))

nMult = 1
dMult = 1
for f in fracList:
	newTerms = reduceTerms(f)
	print(newTerms)
	nMult = nMult * newTerms[0]
	dMult = dMult * newTerms[1]

print(dMult)
