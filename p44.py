import math

def pentagon(n):
	return n * (3*n - 1) / 2

def is_pentagon(n):
	nr = (math.sqrt(n*24+1)+1)/6
	if int(nr) == nr:
		return True
	return False

pentagons = []

for i in range(1, 2000):
	for j in range(i, 2000):
		a,b = pentagon(i), pentagon(j)
		if is_pentagon(a + b):
			if is_pentagon(a + 2*b):
				print(a)
			elif is_pentagon(2*a + b):
				print(b)