





#guess
minFrac = [1, 8]
mFrac = minFrac[0]/minFrac[1]
#The fraction directly to the right of our answer
target = [3, 7]
tFrac = target[0]/target[1]

for denom in range(1, 1000001):
	if not denom % 10000:
		print(denom)

	#This give us an estimate for the numerator
	num = int(denom * (3/7))

	if num / denom < tFrac:
		if num / denom > mFrac:
			minFrac = [num, denom]
			mFrac = minFrac[0]/minFrac[1]


print(minFrac)