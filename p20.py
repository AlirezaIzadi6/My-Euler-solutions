number = 1
for i in range(1, 101):
	number *= i

result = 0
while number > 0:
	result += number%10
	number = number // 10

print(result)