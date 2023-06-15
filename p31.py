from itertools import combinations

def changer(coin, coins):
	result = 0
	noc = [0 for _ in range(len(coins))]
	csum = 0 # sum of coins sent to the function
	for c in coins:
		csum += c
	if coin < csum:
		return 0
	if len(coins) == 1:
		if coin%coins[0] != 0:
			return 0
		return 1
	elif len(coins) > 1:
		for i in range(len(coins)):
			noc[i] = (coin + coins[i] - csum) // coins[i] + 1
		if len(coins) == 2:
			for i in range(1, noc[0]):
				for j in range(1, noc[1]):
					if i*coins[0] + j*coins[1] == coin:
						result += 1
		elif len(coins) == 3:
			for i in range(1, noc[0]):
				for j in range(1, noc[1]):
					for k in range(1, noc[2]):
						if i*coins[0] + j*coins[1] + k*coins[2] == coin:
							result += 1
		elif len(coins) == 4:
			for i in range(1, noc[0]):
				for j in range(1, noc[1]):
					for k in range(1, noc[2]):
						for l in range(1, noc[3]):
							if i*coins[0] + j*coins[1] + k*coins[2] + l*coins[3] == coin:
								result += 1
		elif len(coins) == 5:
			for i in range(1, noc[0]):
				for j in range(1, noc[1]):
					for k in range(1, noc[2]):
						for l in range(1, noc[3]):
							for m in range(1, noc[4]):
								if i*coins[0] + j*coins[1] + k*coins[2] + l*coins[3] + m*coins[4] == coin:
									result += 1
		elif len(coins) == 6:
			for i in range(1, noc[0]):
				for j in range(1, noc[1]):
					for k in range(1, noc[2]):
						for l in range(1, noc[3]):
							for m in range(1, noc[4]):
								for n in range(1, noc[5]):
									if i*coins[0] + j*coins[1] + k*coins[2] + l*coins[3] + m*coins[4] + n*coins[5] == coin:
										result += 1
		elif len(coins) == 7:
			for i in range(1, noc[0]):
				for j in range(1, noc[1]):
					for k in range(1, noc[2]):
						for l in range(1, noc[3]):
							for m in range(1, noc[4]):
								for n in range(1, noc[5]):
									for o in range(1, noc[6]):
										if i*coins[0] + j*coins[1] + k*coins[2] + l*coins[3] + m*coins[4] + n*coins[5] + o*coins[6] == coin:
											result += 1
	return result

result = 0
coins = [100, 50, 20, 10, 5, 2, 1]
list_of_combinations = list()
for n in range(1, len(coins)+1):
	list_of_combinations += [list(c) for c in combinations(coins, n)]

list_of_combinations.sort()
last_combination = [0]

for c in list_of_combinations:
	if last_combination == c:
		continue
	last_combination = c
	result += changer(200, c)

print(result+1)