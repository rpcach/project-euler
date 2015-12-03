def main():
	array = [1,2,5,10,20,50,100,200]

	count = 0
	sum = 0

	for a in range(0,201):
		sumA = array[0]*a
		for b in range(0,101):
			sumB = sumA + array[1]*b
			if sumB > 200: break
			for c in range(0,41):
				sumC = sumB + array[2]*c
				if sumC > 200: break
				for d in range(0,21):
					sumD = sumC + array[3]*d
					if sumD > 200: break
					for e in range(0,11):
						sumE = sumD + array[4]*e
						if sumE > 200: break
						for f in range(0,5):
							sumF = sumE + array[5]*f
							if sumF > 200: break
							for g in range(0,3):
								sumG = sumF + array[6]*g
								if sumG > 200: break
								for h in range(0,2):
									sumH = sumG + array[7]*h
									if sumH > 200: break
									if sumH == 200:
										count += 1
										#print(count)
	print(count)
main()