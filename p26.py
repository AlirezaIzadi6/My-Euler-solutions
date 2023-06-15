max = 0
result = 0
for i in range(1, 1000):
	n = str(10**10000//i)
	while n[-1] == '0':
		n = n[:-1]
	for j in range(1, len(n)//2):
		if n[:j] == n[j:2*j]:
			if j > max:
				max = j
				result = i
			break

print(result)