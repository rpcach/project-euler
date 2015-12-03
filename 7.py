import math

def main():
	count = 2
	x = 5

	while count != 10001:
		count += isPrime(x)
		x += 2
	
	print(x-2)

def isPrime(num):
	for x in xrange(3,int(math.sqrt(num))+1,2):
		if num % x == 0:
			return 0
	return 1

main()