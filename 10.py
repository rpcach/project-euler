import math

def main():
	total = 5

	for x in xrange(5,2000000,2):
		if isPrime(x):
			total += x

	print(total)

def isPrime(num):
	for x in xrange(3,int(math.sqrt(num))+1,2):
		if num % x == 0:
			return 0
	return 1
	
main()