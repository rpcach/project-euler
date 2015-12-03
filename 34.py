def main():
	sum = 0

	for x in range(3,1000000):
		if x == sumFactorialDigits(x):
			sum += x

	print(sum)

def sumFactorialDigits(x):
	sum = 0

	number = str(x)
	for n in number:
		sum += factorial(int(n))
		#print((int(n)))

	return sum


def factorial(n):
	prod = 1
	for x in range(1,n+1):
		prod *= x

	return prod

main()