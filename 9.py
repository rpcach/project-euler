import math

def main():

	for b in range(4,1000):
		for a in range(3,b):
			c = math.sqrt(a*a+b*b)
			if(a+b+c) == 1000 and c%1 == 0:
				print(a*b*c)
				exit(0)

main()