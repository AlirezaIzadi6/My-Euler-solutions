def reverse_number(n):
	result = 0
	while n > 0:
		result = result * 10 + n%10
		n = n//10
	return result

res = 0
result = ''
for i in range(100, 1000):
	for j in range(i, 1000):
		number = i*j
		if number == reverse_number(number) and number > res:
			res = number

print(res)