def main():
	num = 1

	for x in range(1,100):
		num *= x

	string = str(num)
	total = 0

	for x in string:
		total += int(x)

	print(total)
main()