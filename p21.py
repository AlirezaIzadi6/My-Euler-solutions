import math
result = 0

def sumofdevisers(n):
	result = 0
	nr = math.floor(math.sqrt(n))
	for i in range(2, nr):
		if n%i == 0:
			if i != n//i:
				result = result + i + n//i
			else:
				result += i
	return result+1

for i in range(1, 10000):
	j = sumofdevisers(i)
	if sumofdevisers(j) == i and i < j:
		result = result + i + j

print(result)