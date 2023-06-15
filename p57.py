result = 0
a = 1
b = 2
counter = 0
while counter < 1000:
	if len(str(a+b)) > len(str(b)):
		result += 1
	a, b = b, 2*b + a
	counter += 1

print(result)