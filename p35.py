import math

def is_prime(n):
	if n < 2:
		return False
	r = math.floor(math.sqrt(n))
	for i in range(2, r+1):
		if n%i == 0:
			return False
	return True

def is_circular_prime(n):
	numbers = []
	s = str(n)
	for i in range(len(s)):
		numbers.append(int(s[i:] + s[:i]))
	res = True
	for number in numbers:
		if not is_prime(number):
			return False
	return True

result = 0
for i in range(1, 1000000):
	if is_circular_prime(i):
		result += 1

print(result)