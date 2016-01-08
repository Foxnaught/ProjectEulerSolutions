
singles = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
obtuse = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

textLength = ""
for i in range(1, int(input("Max range: "))+1):
	numString = str(i)[::-1]
	for index in range(numString.__len__()):
		t = numString.__len__() - 1 - index
		if(numString.__len__() > 3 and t==3):
			textLength += "onethousand"
		if numString.__len__() > 2 and t==2 and int(numString[2]) != 0:
			#Get the singular value
			textLength += singles[int(numString[2])-1]
			#Add digit modifier
			textLength += "hundred"
			if(int(numString[0]) > 0 or int(numString[1]) > 0):
				textLength += "and"
		if(numString.__len__() > 1 and t==1) and int(numString[1]) > 1:
			textLength += tens[int(numString[1])-1]
		if numString.__len__() > 1 and t==1 and int(numString[1]) == 1:
			textLength += obtuse[int(numString[0])]
		if t==0 and (numString.__len__() == 1 or int(numString[1]) != 1) and int(numString[0]) != 0:
			print(numString)
			textLength += singles[int(numString[0])-1]
		
		
		
		

print(textLength)
print(textLength.__len__())
