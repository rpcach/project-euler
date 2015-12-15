import math

def main():
	array = [1,3,5,7,9]

	current = 9
	length = 2

	numerator = 3.0
	denominator = 5.0

	while numerator/denominator > .10:
		current += 1
		length += 1
		
		current += length
		if isPrime(current):
			numerator += 1
		length += 1

		current+= length
		if isPrime(current):
			numerator += 1

		current += length
		if isPrime(current):
			numerator += 1

		current += length
		if isPrime(current):
			numerator += 1

		denominator += 4

	print(length+1)


def isPrime(n):
	if n%2 == 0:
		return 0

	for x in xrange(3,int(math.sqrt(n))+1,2):
		if n % x == 0:
			return 0
	return 1

main()