def decimal_to_binary(n):
	result = 0
	counter = 0
	while n > 0:
		result = result+ 10**counter*(n%2)
		n = n//2
		counter += 1
	return result

def is_palindromic(n1):
	n = n1
	n2 = 0
	while n > 0:
		n2 = n2*10 + n%10
		n = n//10
	if n1 == n2:
		return True
	return False

result = 0
for i in range(1, 1000000):
	if is_palindromic(i) and is_palindromic(decimal_to_binary(i)):
		result += i

print(result)