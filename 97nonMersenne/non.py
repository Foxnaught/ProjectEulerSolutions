



exponent = 7830457
coefficient = 28433
value = 1

for i in range(exponent):
	value = value * 2

	if str(value).__len__() > 10:
		temp = str(value)[-10:]
		value = int(temp)


value = value * coefficient
if str(value).__len__() > 10:
	temp = str(value)[-10:]
	value = int(temp)


value += 1

print(value)
