f = []
for i in range(1, 10):
	res = 1
	for j in range(1, i+1):
		res *= j
	f.append(res)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

number = 999999

fIndex = 8
result = 0
while number > 0:
	n = number//f[fIndex]
	result = result*10 + numbers[n]
	numbers.pop(n)
	number = number%f[fIndex]
	fIndex -= 1
	f.pop(fIndex+1)

for n in numbers:
	result = result*10 + n

print(result)