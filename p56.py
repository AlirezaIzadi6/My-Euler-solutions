def sum_of_digits(n):
	result = 0
	while n > 0:
		result += n%10
		n = n//10
	return result

max = 0
for i in range(1, 101):
	for j in range(1, 100):
		s = sum_of_digits(i**j)
		if s > max:
			max = s

print(max)