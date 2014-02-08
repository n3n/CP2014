dayaweek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
dayamonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 31, 31]
year = input()
first_day = input()
month = input()
day = input()
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    dayamonth[1] = 29	
total = day + first_day + sum(dayamonth[:month - 1])
print dayaweek[(total - 1) % 7]
