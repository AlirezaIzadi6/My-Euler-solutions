sum = 0

a = 1
b = 1
while a + b < 4000000:
	a, b = b, a+b
	if b%2 == 0:
		sum += b

print(sum)