def main():
	product = 1

	for x in range(10,99):
		for y in range(x+1,100):
			if isCurious(x,y):
				product *= x
				product /= y

	print(product)

def isCurious(x,y):
	a = str(x)
	b = str(y)

	for i in a:
		if i in b:
			a = a.replace(i,"")
			b = b.replace(i,"")

			if a == "":
				a = i
			if b == "":
				b = i

			if y%10 !=0 and int(a)/int(b) == x/y:
				return 1
			else:
				return 0

main()