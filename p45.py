import math

def is_pentagon(n):
	nr = (math.sqrt(24*n+1)+1)/6
	if int(nr) == nr:
		return True
	return False

def is_hexagon(n):
	nr = (math.sqrt(8*n+1)+1)/4
	if int(nr) == nr:
		return True
	return False

for i in range(500000):
	t = i*(i+1)/2
	if is_pentagon(t) and is_hexagon(t):
		print(t)