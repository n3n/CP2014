day_name  = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year      = input()
first_day = input()
month     = input()
day       = input()

if year%4 == 0   and \
   year%100 == 0 and \
   year%400 == 0 or  \
   (year%4 == 0 and year%100 != 0 ):
    day_month[1] += 1

total_day = sum(day_month[:month-1]) + day - 1
print day_name[(total_day%7+first_day)%7]
