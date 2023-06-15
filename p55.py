def is_palindrome(N):
	result = 0
	n = N
	while n > 0:
		result = result * 10 + n%10
		n = n//10
	if result == N:
		return True
	return False

def reverse_number(n):
	result = 0
	while n > 0:
		result = result * 10 + n%10
		n = n//10
	return result

result = 0
for i in range(10, 10000):
	counter = 0
	is_Lychrel = True
	while counter < 50:
		i = i + reverse_number(i)
		if is_palindrome(i):
			is_Lychrel = False
			break
		counter += 1
	if is_Lychrel:
		result += 1

print(result)