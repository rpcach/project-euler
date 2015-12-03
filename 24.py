import itertools

def main():
	array = list(itertools.permutations('0123456789',10))

	print(array[999999])

main()