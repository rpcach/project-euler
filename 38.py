def main():
	largest = 0

	for x in range(1,10000):
		m = 2
		s = str(x)
		while len(s) < 9:
			s = s + str(m*x)
			m += 1


		if isPandigital(int(s)) and int(s) > largest:
			largest = int(s)

	print(largest)

def isPandigital(n):
	s = str(n)

	if len(s) != 9:
		return 0
	
	digits = [1,2,3,4,5,6,7,8,9]

	for x in digits:
		if str(x) not in s:
			return 0

	return 1

main()