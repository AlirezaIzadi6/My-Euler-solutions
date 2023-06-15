import math

def is_prime(n):
	if n < 2:
		return False
	r = math.floor(math.sqrt(n))
	for i in range(2, r+1):
		if n%i == 0:
			return False
	return True

primes = []
for i in range(100000):
	if is_prime(i):
		primes.append(i)

def number_of_df(n): # df = distinct factors
	result = 1
	if n == 0 or n == 1:
		return 0
	while not (is_prime(n) or n == 1):
		for p in primes:
			if p > math.sqrt(n):
				break
			if n%p == 0 :
				result += 1
				while n%p == 0:
					n /= p
	return result

for i in range(1000000):
	if number_of_df(i) == 4:
		if number_of_df(i+1) == 4 and number_of_df(i+2) == 4 and number_of_df(i+3) == 4:
			print(i)
			break