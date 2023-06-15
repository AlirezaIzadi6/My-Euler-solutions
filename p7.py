import math

counter = 0
result = 0
number = 2

while counter < 10001:
	number_root = math.floor(math.sqrt(number))
	is_prime = True
	for i in range(2, number_root+1):
		if number%i == 0:
			is_prime = False
			break
	if is_prime:
		counter += 1
		result = number
	number += 1

print(result)