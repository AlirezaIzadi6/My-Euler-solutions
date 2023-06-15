import math
number = 600851475143
number_root = math.ceil(math.sqrt(number))
largest_factor = 0
i = 2

while i < number_root:
	if number%i == 0:
		largest_facter = i
		number = number//i
		number_root = math.ceil(math.sqrt(number))
	else:
		i += 1

print(number)