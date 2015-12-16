def main():
	count89 = 0
	array = [0]*10000000

	for x in range(1,10000000):
		xx = x
		x = orderDigits(x)

		if array[x] != 0:
			count89 += 1
			continue

		while x != 1 and x != 89:
			x = sumOfSquareOfDigits(x)

		if x != 1:
			array[xx] = 1
			count89 += 1

	print(count89)

def sumOfSquareOfDigits(n):
	s = str(n)
	sum = 0

	for d in s:
		sum += int(d)*int(d)

	return sum

def orderDigits(n):
	s = str(n)
	s = ''.join(sorted(s))

	return int(s)

main()