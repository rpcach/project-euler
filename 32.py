import math

def main():
	panDigits = []

	for a in range(1,10000):
		for b in range(a,10000):
			c = a*b
			if isPandigital(a,b,c):
				if c not in panDigits:
					panDigits.append(c)
					print(panDigits)
	
	sum = 0
	for x in panDigits:
		sum += x

	print(sum)

		
def isPandigital(a,b,c,):
	abc = str(a) + str(b) + str(c)
	digits = [1,2,3,4,5,6,7,8,9]
	
	if len(abc) != 9:
		return 0

	for x in digits:
		if str(x) not in abc:
			return 0

	return 1

main()