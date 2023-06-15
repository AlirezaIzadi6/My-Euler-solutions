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
for i in range(2, 1000000):
	if is_prime(i):
		primes.append(i)
print('done')

def num_of_primes(n):
	res = 0
	if not is_prime(n):
		return 0
	for i in range(primes.index(n)):
		sum = 0
		counter = 0
		while sum <= n:
			if sum == n:
				return counter
			sum += primes[i+counter]
			counter += 1
	return 0

max = 0
result = 0
for p in primes:
	n = num_of_primes(p)
	if n > max:
		max = n
		result = p

print(result)