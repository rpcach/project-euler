def main():
	char3s = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]
	#8 unique digits: 0,1,2,3,6,7,8,9

	flag = 0
	for passcode in range(10236789, 98765433):
		if '4' in str(passcode) or '5' in str(passcode):
			continue
		for char3 in char3s:
			if not char3inPasscode(str(char3),str(passcode)):
				flag = 0
				break
			flag = 1
		if flag == 1:
			print(passcode)
			exit(0)

def char3inPasscode(char3,passcode):
	counter = 0
	for x in passcode:
		if counter == 3:
			return 1
		if char3[counter] == x:
			counter += 1

	if counter != 3:
		return 0

	return 1

main()