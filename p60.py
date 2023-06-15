import math

primes = []

prime_cache = {}
def is_prime(n):
	if prime_cache.get(n):
		return True
	if n < 2:
		return False
	r = math.floor(math.sqrt(n))
	for i in range(2, r+1):
		if n%i == 0:
			return False
	prime_cache[n] = 1
	return True

def check_set(s):
	for i in range(len(s)-1):
		for j in range(i+1, len(s)):
			if not (is_prime(s[i]*10**len(str(s[j]))+s[j]) and is_prime(s[j]*10**len(str(s[i]))+s[i])):
				return False
	return True

for i in range(3, 100000, 2):
	if is_prime(i):
		primes.append(i)

max = len(primes)

def change_max(n):
	MyPrimes = primes + [n]
	MyPrimes.sort()
	Max = MyPrimes.index(n)
	return Max

for i in range(max):
	if i%100 == 0:
		print(i)
	set = [primes[i]]
	for j in range(i+1, max):
		if check_set(set + [primes[j]]):
			set.append(primes[j])
			for k in range(j+1, max):
				if check_set(set + [primes[k]]):
					set.append(primes[k])
					for l in range(k+1, max):
						if check_set(set + [primes[l]]):
							set.append(primes[l])
							for m in range(l+1, max):
								if check_set(set + [primes[m]]):
									set.append(primes[m])
									result = 0
									for s in set:
										result += s
									print(set)
									exit()
									max = change_max(result)
