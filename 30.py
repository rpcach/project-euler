def main():
	sum = 0

	for x in range(2,1000000):
		if sumOfFifths(x) == x:
			sum += x

	print(sum)

def sumOfFifths(n):
	string = str(n)
	sum = 0
	for d in string:
		sum += pow(int(d),5)

	return sum


def pow(a,b):
	prod = 1

	for x in range(0,b):
		prod *= a

	return prod

main()