def digitcount(n):
	res = 0
	while n > 0:
		n = n//10
		res += 1
	return res

newnumber = 1
oldnumber = 0
counter = 1

while digitcount(newnumber) < 1000:
	oldnumber, newnumber = newnumber, newnumber+oldnumber
	counter += 1

print(counter)