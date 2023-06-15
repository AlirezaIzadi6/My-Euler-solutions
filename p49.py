import math

def is_prime(n):
	if n < 2:
		return False
	r = math.floor(math.sqrt(n))
	for i in range(2, r+1):
		if n%i == 0:
			return False
	return True

def factorial(n):
	result = 1
	for i in range(1, n+1):
		result *= i
	return result

def permutations(n):
	result = []
	Digits = []
	while n > 0:
		Digits.append(n%10)
		n = n//10
	for i in range(factorial(len(Digits))):
		digits = Digits[:]
		res = 0
		while len(digits) > 0:
			I = i//factorial(len(digits)-1)
			res = res*10 + digits[I]
			i = i%factorial(len(digits)-1)
			digits.pop(I)
		result.append(res)
	result = list(dict.fromkeys(result))
	result.sort()
	return result

for i in range(1001, 10000, 2):
	if not is_prime(i):
		continue
	perm = permutations(i)
	prime_perms = []
	for p in perm:
		if is_prime(p) and p > 1000:
			prime_perms.append(p)
	for i in range(len(prime_perms)-2):
		for j in range(i+1, len(prime_perms)-1):
			d = 2*prime_perms[j] - prime_perms[i]
			if d in prime_perms:
				print('{0}, {1}, {2}'.format(prime_perms[i], prime_perms[j], d))
				break