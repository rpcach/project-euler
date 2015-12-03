def main():
	a = 0
	b = 1
	c = a+b

	count = 0
	eventotal = 0

	while b < 4000000:
		c = a+b
		a = b
		b = c

		if b % 2 == 0:
			eventotal += b
	
	print(eventotal)

main()