def main():
	total = 0

	for x in range(1,1000):
		print(x)
		if x%3 == 0 or x%5 == 0:
			total += x
	print(total)

main()