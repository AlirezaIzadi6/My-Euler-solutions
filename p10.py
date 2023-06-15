import math

def is_prime(n):
	r = math.floor(math.sqrt(n))
	for i in range(2, r+1):
		if n%i == 0:
			return False
	return True

sum=0
for i in range(2, 2000000):
	if is_prime(i):
		sum += i

print(sum)