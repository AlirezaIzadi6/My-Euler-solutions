def get_factorial(n):
	res = 1
	for i in range(1, n+1):
		res *= i
	return res

result = get_factorial(40) // (get_factorial(20)**2)
print(result)