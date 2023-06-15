def has_repetetive_digits(l):
	digits = []
	for n in l:
		while n > 0:
			digits.append(n%10)
			n = n// 10
	if len(digits) > len(list(dict.fromkeys(digits))) or len(digits) < 9 or 0 in digits:
		return False
	if len(digits) < 9:
		return False
	return True

pandigitals = []
for a in range(10, 100):
	for b in range(100, 1000):
		if has_repetetive_digits([a, b, a*b]):
			pandigitals.append(a*b)

for a in range(1, 10):
	for b in range(1000, 10000):
		if has_repetetive_digits([a, b, a*b]):
			pandigitals.append(a*b)


pandigitals = list(dict.fromkeys(pandigitals))
result = 0
for n in pandigitals:
	result += n
print(result)