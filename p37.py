import math

def is_prime(n):
	if n < 2:
		return False
	r = math.floor(math.sqrt(n))
	for i in range(2, r+1):
		if n%i == 0:
			return False
	return True

def is_truncatable(n):
	s = str(n)
	while len(s) > 0:
		if not is_prime(int(s)):
			return False
		else:
			s = s[:-1]
	s = str(n)
	while len(s) > 0:
		if not is_prime(int(s)):
			return False
		else:
			s = s[1:]
	return True

tps = []
counter = 10
result = 0
while len(tps) < 11:
	if is_truncatable(counter):
		tps.append(counter)
		result += counter
	counter += 1

print(result)