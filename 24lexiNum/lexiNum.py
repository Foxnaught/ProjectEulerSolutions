

def lexiPerm(n):
	permList = []
	newList = []
	perms = []
	nLen = len(n)

	if nLen > 2:
		for i in range(nLen):
			newList = n[:]
			newList.pop(i)

			perms = lexiPerm(newList)
			for p in perms:
				permList.append([n[i]] + p)

	elif nLen == 2:
		permList.extend([n, [n[1], n[0]]])
	else:
		permList = [n]

	return permList


n = int(input("Lexi range: "))
valArray = list(range(n))

#Only works for n = 10
millionth = ""
for s in sorted(lexiPerm(valArray))[999999]:
	millionth += str(s)

print(millionth)





