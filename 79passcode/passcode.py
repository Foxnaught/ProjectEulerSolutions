

f = open('keylog.txt', 'r')

entryList = []
line = f.readline()
while line:
	entryList.append(line)
	line = f.readline()

entryList = list(set(entryList))

p = open('filter.txt', 'w')
for e in entryList:
	p.write(e)
p.close()

f.close()




