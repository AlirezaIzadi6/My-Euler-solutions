import math

def has_repetetive_digits(n):
	digits = []
	digits_n = 0
	while n > 0:
		digits.append(n%10)
		n = n// 10
		digits_n += 1
	numbers = []
	for i in range(1, digits_n+1):
		numbers.append(i)
	if len(digits) > len(list(dict.fromkeys(digits))):
		return False
	for n in digits:
		if n not in digits_n:
			return False
	return True

def is_prime(n):
	if n < 2:
		return False
	r = math.floor(math.sqrt(n))
	for i in range(2, r+1):
		if n%i == 0:
			return False
	return True

def factorial(n):
	res = 1
	for i in range(2, n+1):
		res *= i
	return res

f = []
for i in range(0, 10):
	f.append(factorial(i))

result = 0
for i in range(1, 10):
	for j in range(f[i]):
		numbers = [I for I in range(1, i+1)]
		res = 0
		while len(numbers) > 0:
			c = i - len(numbers) + 1
			J = j//f[i-c]
			res = res*10 + numbers[J]
			j = j%f[i-c]
			numbers.pop(J)
		if is_prime(res) and res > result:
			result = res

print(result)