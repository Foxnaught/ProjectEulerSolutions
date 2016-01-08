

#Recursively build composite numbers while testing their pandigitalness
#As n is combined with other primes it's totient value is passed so that only the totient of the new prime must be evaluated
#The totient of any prime p is : phi(p) = p - 1
def totRec(n, nTot, header=0):
	global primes
	global primeLen
	global limit
	minP = False
	pTot = False
	#Each level exhaustes all multiples of a given prime
	#So the next level can skip all primes before it
	for i in range(header, primeLen - header):
		p = primes[i]
		if p * n < limit:
			#Basic case, we are still below the limit so let's check if this multiple and it's totient have a lower ratio and are pandigital to each other
			if (not minP or (n*p)/(nTot * (p-1)) < minP/pTot) and sorted(str(n*p)) == sorted(str(nTot * (p-1))):
				minP = n * p
				pTot = nTot * (p-1)


			#Recursive call
			permVal = totRec(n * p, nTot * (p-1), i+1)
			#If we found more pandigital multiples below the limit in the recursive call then let's check if it has a lower ratio than what we can currently see
			if permVal[0]:
				if not minP or permVal[0]/permVal[1] < minP/pTot:
					minP = permVal[0]
					pTot = permVal[1]
		else:
			break

		
	#pass the n value and it's totient that has the lowest ratio on this level
	#returns false in both values if no pandigital ratio is found
	return [minP, pTot]

def SOE(n):
	numList = list(range(n))
	primes = [2]
	for i in range(3, n, 2):
		if numList[i]:
			primes.append(i)

			mult = 3
			while i * mult < n:
				numList[i*mult] = 0
				mult += 2

	return primes

limit = 10000000
limit = 10000000
primes = SOE(int(limit + limit * .1))
primeLen = len(primes)


#The first value is our n
#The second value is our phi(n)
print(totRec(1, 1))





