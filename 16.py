def main():
	exponent = 1
	num = 2

	while exponent < 1000:
		exponent += 1
		num *= 2

	string = str(num)
	total = 0
	
	for x in string:
		total += int(x)

	print(total)


main()