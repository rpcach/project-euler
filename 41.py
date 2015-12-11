import math

def main():
	largest = 0
	for x in xrange(3,100000000,2):
		if isPandigital(x) and isPrime(x):
				largest = x
				print(x)

	print(largest)

def isPrime(n):
	if n%5 == 0 or n%3 == 0:
		return 0

	for x in xrange(7,int(math.sqrt(n))+1,2):
		if n % x == 0:
			return 0
	return 1

def isPandigital(n):
	s = str(n)
	length = len(s) + 1

	if '0' in s:
		return 0

	for x in range(1,length):
		if str(x) not in s:
			return 0

	return 1

main()