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
for i in range(2, 1000):
	if is_prime(i):
		primes.append(i)
		primes.append(-i)

max = 0
result = 0

for a in range(-999, 1000):
	for b in primes:
		score = 0
		while is_prime(score**2 + a*score + b):
			score += 1
		if score > max:
			max = score
			result = a*b

print(max)