import math

def is_prime(n):
	if n < 2:
		return False
	r = math.floor(math.sqrt(n))
	for i in range(2, r+1):
		if n%i == 0:
			return False
	return True

corners = [1]
primes = []
for i in range(3, 1000000, 2):
	for j in range(4):
		c = i**2 - j*(i**2 - (i-2)**2)/4
		corners.append(c)
		if is_prime(c):
			primes.append(c)
	if len(primes)/len(corners) < 0.1:
		print(i)
		break