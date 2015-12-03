def main():

	longest = 1	
	start = 1

	for x in range(1,1000000):
		n = collatzNext(x)
		length = 2

		while n != 1:
			n = collatzNext(n)
			length += 1
		if length > longest:
			longest = length
			start = x

	print(start)

def collatzNext(n):
	if n%2 == 0:
		n /= 2
	else:
		n = 3*n + 1
	return n


main()