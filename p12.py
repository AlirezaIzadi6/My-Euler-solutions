import math

number_of_devisers = 0
number = 0
counter = 1

while number_of_devisers <= 500:
	number_of_devisers = 0
	number += counter
	counter += 1
	for i in range(1, math.floor(math.sqrt(number))+1):
		if number%i == 0:
			number_of_devisers += 2
			if i**2 == number:
				number_of_devisers -= 1

print(number)