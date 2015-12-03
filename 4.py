def main():
	largest = 0

	for x in range(100,999):
		for y in range(100,999):
			num = x*y
			b = str(num)
			c = b[::-1]
			if b == c and num > largest:
				largest = num
	print(largest)

main()