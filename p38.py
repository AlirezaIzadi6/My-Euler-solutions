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

result = 0
for i in range(1, 340000):
	res = ''
	counter = 1
	while len(res) < 9:
		res += str(i*counter)
		counter += 1
	if has_repetetive_digits([int(res)]):
		if int(res) > result:
			result = int(res)

print(result)