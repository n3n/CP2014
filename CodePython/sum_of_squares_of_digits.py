def sum_of_squares_of_digits(n):
    '''check input digits , return number of digits'''
    count,num = 0,0
    i, m = 10, 10
    n = abs(n)
    while n/i > 0:
        count += 1
        i *= 10
    while i >= 10:
        i = m**count
        c = n/i
        n = n-(c*i)
        num = num + (c**2)
        count -= 1
    return num
print sum_of_squares_of_digits(987)
