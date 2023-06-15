def factorial(n):
	result = 1
	if n == 1 or n == 0:
		return 1
	for i in range(1, n+1):
		result *= i
	return result

f = []
for i in range(0, 101):
	f.append(factorial(i))

result = 0
for i in range(100, 0, -1):
	for j in range(i, 0, -1):
		n = f[i]
		r = f[j]
		if n/(r*f[i-j]) > 1000000:
			result += 1

print(result)