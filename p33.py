def compair(a, b):
	if(a//10 != b%10 and a%10 != b//10):
		return False
	if a%10 == 0 or a//10 == 0 or b//10 == 0 or b%10 == 0 or a//10 == a%10 or b//10 == b%10:
		return False
	r1 = a/b
	r2 = 0
	if a//10 == b%10:
		r2 = (a%10) / (b//10)
	elif a%10 == b//10:
		r2 = (a//10) / (b%10)
	if r1 == r2:
		return True
	return False

num = 1
denum = 1
for i in range(10, 50):
	for j in range(i, 100):
		if compair(i, j):
			num *= i
			denum *= j

for i in range(2, min(num, denum)):
	while num%i == 0 and denum%i == 0:
		num /= i
		denum /= i

print(denum)