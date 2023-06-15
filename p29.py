numbers = []
for a in range(2, 101):
	for b in range(2, 101):
		numbers.append(a**b)

numbers = list(dict.fromkeys(numbers))
numbers.sort()
print(len(numbers))