import math

def main():
	sum = 0

	for a in range(1,10000):
		b = sumOfDivisors(a)
		if sumOfDivisors(b) == a and a!=b:
			sum += a

	print(sum)

def sumOfDivisors(n):
	sum = 0
	for x in range(1,n):
		if n%x == 0:
			sum += x

	return sum

main()