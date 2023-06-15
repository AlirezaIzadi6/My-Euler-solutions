text = ''

for i in range(1, 1000000):
	if len(text) > 1000000:
		break
	text += str(i)

result = 1
for i in range(7):
	result *= int(text[10**i-1])

print(result)