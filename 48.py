def main():
	sum = 0
	
	for x in range(1,1001):
		sum += selfPower(x)

	print(sum % 10000000000)

def selfPower(n):
	prod = 1
	
	for x in range(0,n):
		prod *= n

	return prod

main()