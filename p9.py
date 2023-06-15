for a in range(1, 1000):
	for b in range(a, 500):
		c = 1000-a-b
		if a**2 + b**2 == c**2:
			print('{0} * {1} * {2} equals {3}'.format(a, b, c, a*b*c))
