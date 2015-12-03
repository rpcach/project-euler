def main():
	x = 1
	add = 2
	sum = x
	
	while x < 1002001:
		x += add
		sum += x
		x += add
		sum += x
		x += add
		sum += x
		x += add
		sum += x

		add += 2

	print(sum)

main()