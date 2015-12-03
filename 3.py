#isPrime is not a correct function
import math

def main():
	num = 600851475143

	for x in range(3,int(math.ceil(math.sqrt(600851475143))),2):
		if num % x == 0:
			print(x)
			if isPrime(x) == 1:
				print(x)
				print('isPrime')

def isPrime(num):
	for x in range(3,int(math.floor(math.sqrt(num))),2):
		if num % x == 0:
			return 0
	return 1

main()