A = [[1 for i in range(1001)] for j in range(1001)]

n = 1
base = 500

for a in range(1, base+1):
	i = 1-a
	j = a
	while True:
		n += 1
		A[base+i][base+j] = n
		if i == -a and j == a:
			break
		if j == a and i != a:
			i += 1
		elif i == a and j != -a:
			j -= 1
		elif j == -a and i != -a:
			i -= 1
		elif i == -a and j != a:
			j += 1

sum = 0
for i in range(1001):
	sum = sum + A[i][i] + A[1000-i][i]

print(sum-1)