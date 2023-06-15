def factorial(n):
	res = 1
	for i in range(2, n+1):
		res *= i
	return res

def sum_of_factorials(n):
	res = 0
	while n > 0:
		res += factorial(n%10)
		n = n//10
	return res

sum = 0
for i in range(3, 1000000):
	if i == sum_of_factorials(i):
		sum += i

print(sum)