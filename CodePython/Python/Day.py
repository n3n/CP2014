year = input()
firstday = input()
month = input()
day = input()
daystr = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
daymonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 31, 31]
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
	daymonth[1] = 29
	
totalday = sum(daymonth[0:month - 1]) + day + firstday
print sum(daymonth[0:month - 1]) + day + firstday , daystr[(totalday - 1) % 7]
