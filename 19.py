def main():
	year = 1901
	day = 2
	month = 0
	array = [31,28,31,30,31,30,31,31,30,31,30,31]
	count = 0

	while year < 2001:
		
		day += array[month]
		if month == 1 and leapyear(year):
			day += 1
		day %= 7

		month += 1
		month %= 12

		if day == 0:
			count += 1
			print(month)
		if month == 0:
			year += 1
	print(count)

def leapyear(year):
	if year%4 == 0:
		if year%100 == 0 and year%400 != 0:
			return 0
		return 1
	else:
		return 0

main()