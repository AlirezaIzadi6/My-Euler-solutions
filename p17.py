n_to_s = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety'}

def convert_to_letters(n):
	result = ''
	if n == 1000:
		return 'onethousand'
	if n >= 100:
		result = n_to_s[str(n//100)] + 'hundred'
		if n%100 != 0:
			result += 'and'
		else:
			return result
	n = n%100
	if n < 20 or n%10 == 0:
		result += n_to_s[str(n)]
	else:
		result = result + n_to_s[str(n-n%10)] + n_to_s[str(n%10)]
	return result

sum = 0
for i in range(1, 1001):
	sum += len(convert_to_letters(i))

print(sum)