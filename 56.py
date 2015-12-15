def main():
	largest = 0

	for x in range(1,100):
		for y in range(1,100):
			z = digitalSum(pow(x,y))
			if z > largest:
				largest = z

	print(largest)

def pow(a,b):
	prod = 1
	for x in range(0,b):
		prod *= a

	return prod

def digitalSum(n):
	s = str(n)
	sum = 0

	for x in s:
		sum += int(x)

	return sum

main()