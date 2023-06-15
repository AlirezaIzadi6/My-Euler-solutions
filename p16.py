n = 2**1000

result = 0
while n > 0:
	result += n%10
	n = n//10

print(result)