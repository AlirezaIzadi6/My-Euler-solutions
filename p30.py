def sum_of_powered_digits(n):
	res = 0
	while n > 0:
		res += (n%10)**5
		n = n//10
	return res

result = 0
for i in range(2, 200000):
	if i == sum_of_powered_digits(i):
		result += i

print(result)