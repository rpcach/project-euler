import math

def main():
	tri_num = 0
	a = 1

	while True:
		tri_num += a
		a += 1

		if numFactors(tri_num) > 500:
			print(tri_num)
			break

def numFactors(n):
	count = 0

	for i in range(1, int(math.sqrt(n))):
		if n % i == 0:
			count += 2

	if n % math.sqrt(n) == 0:
		count += 1

	return count

main()



