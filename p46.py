import math

def is_prime(n):
	if n < 2:
		return False
	r = math.floor(math.sqrt(n))
	for i in range(2, r+1):
		if n%i == 0:
			return False
	return True

for i in range(3, 1000000, 2):
	if is_prime(i):
		continue
	bound = math.ceil(math.sqrt(i/2))
	answer_found = False
	for j in range(1, bound):
		if is_prime(i-(2*j**2)):
			answer_found = True
			break
	if not answer_found:
		print(i)
		break