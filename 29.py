def main():
	array = []
	prod = 1
	for x in range(2,101):
		prod = x
		for y in range(2,101):
			prod *= x
			array.append(prod)

	array.sort()
	array.append(0)
	count = 0
	for x in range(0,len(array)-1):
		if array[x] != array[x+1]:
			count += 1

	print(count)


main()