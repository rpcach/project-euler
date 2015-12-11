import math

def main():
	truncPrimes = []

	for x in range(11,1000000):
		if isPrime(x) and isPrimeTrunctateL2R(x) and isPrimeTrunctateR2L(x):
			truncPrimes.append(x)
		if len(truncPrimes) == 11:
			break

	sum = 0
	
	for x in truncPrimes:
		sum += x

	print(truncPrimes)
	print(sum)

def isPrimeTrunctateL2R(n):
	s = str(n)
	s = s[1:]

	while s != '':
		if not isPrime(int(s)):
			return 0

		s = s[1:]

	return 1

def isPrimeTrunctateR2L(n):
	n = n//10
	
	while n > 0:
		if not isPrime(n):
			return 0

		n = n//10

	return 1

def isPrime(n):
	if n < 2:
		return 0

	if n == 2:
		return 1

	if n%2 == 0:
		return 0

	for x in xrange(3,int(math.sqrt(n))+1,2):
		if n % x == 0:
			return 0
	return 1

main()