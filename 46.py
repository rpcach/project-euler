import math

def main():
	array = []

	for x in range(1,100000):
		array.append(2*x*x)

	x = 3
	while True:
		if not isPrime(x) and not conjectureWorks(x,array):
			print(x)
			break
		x += 2
	print('done')

def conjectureWorks(n,array):
	for y in array:
		if isPrime(n-y):
			return 1

	return 0

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