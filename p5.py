import math

result = 1
primes = [2, 3, 5, 7, 11, 13, 17, 19]

for n in primes:
	n_pow = n
	while n_pow*n < 20:
		n_pow = n_pow * n
	result = result * n_pow

print(result)