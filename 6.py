def main():
	num = 1

	sumOfsquares = 0
	squareOfsum = 0

	for x in range(1,100+1):
		sumOfsquares += (x*x)
		squareOfsum += x
	squareOfsum *= squareOfsum

	print(squareOfsum - sumOfsquares)

main()