import math

def main():
	#print(isPrime(94))

	product = 1
	for x in range(1,100):
		if isPrime(x) == 1:
			print(x)
			if (1/x) %100000000000000000000000000 != 0:
				print((1/x)%1000000000000000000000000)
				product *= x
				print(x)

	print(product)

def isPrime(num):
	if num % 2 == 0:
		return 0
	for x in range(3,int(math.sqrt(num)+1)):
		if num % x == 0:
			return 0
	return 1

#def isRational(num)


main()