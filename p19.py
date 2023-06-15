months = [0, 3, 3, 6, 8, 11, 13, 16, 19, 21, 24, 26]
lmonths = [0, 3, 4, 7, 9, 12, 14, 17, 20, 22, 25, 27]

result = 0
yearday = 0
for year in range(1, 101):
	yday = yearday
	if year%4 == 0:
		mon = lmonths
		yearday += 2
	else:
		mon = months
		yearday += 1
	for m in mon:
		if (yday + m)%7 == 5:
			result += 1

print(result)