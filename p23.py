import math
result = 0

def sumofdevisers(n):
	result = 0
	nr = math.floor(math.sqrt(n))
	for i in range(2, nr+1):
		if n%i == 0:
			if i != n//i:
				result = result + i + n//i
			else:
				result += i
	return result+1

abundents = []
for i in range(1, 28123):
	if i < sumofdevisers(i):
		abundents.append(i)

sums = []
for i in range(len(abundents)):
	for j in range(i, len(abundents)):
		if abundents[i] + abundents[j] < 28124:
			sums.append(abundents[i]+abundents[j])

final_sums = list(dict.fromkeys(sums))

sum = 0
for i in range(28124):
	sum += i

for n in final_sums:
	sum -= n


print(sum)