import math

def main():
	count = 4 #2,3,5,7 are circular primes

	for x in xrange(11,1000000,2):
		if isPrime(x) and isCircularPrime(x):
			count += 1

	print(count)

def isCircularPrime(n):
	for x in range(1,6):
		n = rotate(n)
		if not isPrime(n):
			return 0

	return 1

def rotate(n):
	r = n%10
	n = n//10

	return int(str(r)+str(n))

def isPrime(n):
	if n%2 == 0:
		return 0

	for x in xrange(3,int(math.sqrt(n))+1,2):
		if n % x == 0:
			return 0
	return 1

main()