import math

def main():
	num = 1

	for x in range(11,20+1):
		if num%x != 0:
			for y in range(1,x+1):
				if num*y % x == 0:
					num = num*y
					break

	print(num)

main()