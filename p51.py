import math

def is_prime(n):
	if n < 2:
		return False
	r = math.floor(math.sqrt(n))
	for i in range(2, r+1):
		if n%i == 0:
			return False
	return True

def factorial(n):
	result = 1
	for i in range(1, n+1):
		result *= i
	return result

def permutations(n):
	result = []
	Digits = []
	while n > 0:
		Digits.append(n%10)
		n = n//10
	for i in range(factorial(len(Digits))):
		digits = Digits[:]
		res = 0
		while len(digits) > 0:
			I = i//factorial(len(digits)-1)
			res = res*10 + digits[I]
			i = i%factorial(len(digits)-1)
			digits.pop(I)
		result.append(res)
	result = list(dict.fromkeys(result))
	result.sort()
	return result

def make_patterns(n):
	base = int('2'*n + '111')
	patterns = permutations(base)
	return patterns

def p_increment(p):
	n = int(str(p).replace('2', '0')) * 10
	return n

def get_numbers(p):
	numbers = []
	pattern = str(p)
	twos = []
	for i in range(len(pattern)):
		if pattern[i] == '2':
			twos.append(i)
	if len(twos) == 0:
		return [0]
	start = 0
	if twos[0] == 0:
		start = 10**(len(twos)-1)
	for i in range(start, 10**len(twos)):
		base = pattern.replace('1', '0').replace('2', 'd')
		i_str = str(i).zfill(len(twos))
		for t in twos:
			base = base.replace('d', i_str[0], 1)
			i_str = i_str[1:]
		number = int(base)*10 + 3
		numbers.append(number)
	return numbers

for i in range(4):
	patterns = make_patterns(i)
	for p in patterns:
		inc = p_increment(p)
		p_var = get_numbers(p)
		for v in p_var:
			score = 0
			for j in range(10):
				if is_prime(v + j*inc):
					score += 1
			if score > 7:
				print(v)