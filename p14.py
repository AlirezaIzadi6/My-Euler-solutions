max = 0
result = 0

for i in range(1, 1000000):
	score = 0
	n = i
	while n != 1:
		if n%2 == 0:
			n = n / 2
		else:
			n = n * 3 + 1
		score += 1
	if score > max:
		max = score
		result = i

print(result)