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

def check_permutation(n1, n2):
	d1 = []
	d2 = []
	while n1 > 0:
		d1.append(n1%10)
		n1 = n1//10
	while n2 > 0:
		d2.append(n2%10)
		n2 = n2//10
	d1.sort()
	d2.sort()
	if d1 == d2:
		return True
	return False

i = 1
while True:
	if check_permutation(i, 2*i) and check_permutation(i, 3*i) and check_permutation(i, 4*i) and check_permutation(i, 5*i) and check_permutation(i, 6*i):
		print(i)
		break
	i += 1