def factorial(n):
	res = 1
	for i in range(2, n+1):
		res *= i
	return res

f = []
for i in range(0, 11):
	f.append(factorial(i))

result = 0
for i in range(f[10]):
	numbers = [I for I in range(10)]
	res = 0
	while len(numbers) > 0:
		c = 10 - len(numbers) + 1
		I = i//f[10-c]
		res = res*10 + numbers[I]
		i = i%f[10-c]
		numbers.pop(I)
	if int(str(res)[1:4])%2 == 0 and int(str(res)[2:5])%3 == 0 and int(str(res)[3:6])%5 == 0 and int(str(res)[4:7])%7 == 0 and int(str(res)[5:8])%11 == 0 and int(str(res)[6:9])%13 == 0 and int(str(res)[7:])%17 == 0:
		result += res

print(result)