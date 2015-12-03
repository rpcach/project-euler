def main():

	array = []
	
	for x in range(0,21):
		array.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

	
	for x in range(1,21):
		array[x][0] = 1
		array[0][x] = 1

	for x in range(1,21):
		for y in range(1,21):
			array[x][y] = array[x-1][y]+array[x][y-1]

	print(array[20][20])

main()