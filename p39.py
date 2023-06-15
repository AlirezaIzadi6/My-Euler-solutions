import math

p = [0 for i in range(1001)]

def is_square(n):
	if n//math.sqrt(n) == math.sqrt(n):
		return True
	return False

for a in range(1, 340):
	for b in range(a, 500):
		c2 = a**2 + b**2
		c = int(math.sqrt(c2))
		if is_square(c2) and a+b+c <= 1000:
			p[a + b + c] += 1

print(p.index(max(p)))