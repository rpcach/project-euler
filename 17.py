one = [0,3,3,5,4,4,3,5,5,4] #'0'-9
ten = [0,0,6,6,5,5,5,7,6,6] #'00',10',20,30,...,90
ven = [3,6,6,8,8,7,7,9,8,8] #'10',11,12,13,...,19
#hundred[] = 

def main():
	sum = 0
	for x in range(1,1000):
		sum += ones(x)
		sum += tens(x)
		sum += hundreds(x)

	sum += 11 #1000
	print(sum)

def ones(x):
	d = x%10
	if d == 0:
		return 0

	return one[d]

def tens(x):
	d = (x//10)%10 #tens digit
	if d == 0:
		return 0

	if d == 1:
		return ven[x%10]-ones(x)
	else:
		return ten[d]

def hundreds(x):
	d = (x//100)%100 #hundreds digit
	if d == 0:
		return 0

	if x%100 != 0:
		return one[d] + 10 #(with 'and')
	else:
		return one[d] + 7 #(without 'and')

main()