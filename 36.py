import math

def main():
	total = 0
	
	for x in range(1,1000000):
		if palindromic(x) and palindromic(b2(x)):
			total += x

	print(total)

def palindromic(n):
	if str(n) == str(n)[::-1]:
		return 1

	return 0

def b2(n):
	stringN = bin(n)
	stringN = stringN.replace("0b","")

	return int(stringN)

main()