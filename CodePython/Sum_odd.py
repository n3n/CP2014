n = input()
def sum_number_v2(n):
    count = 0
    while n >= 0:
        if n % 2 == 1:
            count += n
        n -= 1
    print count
sum_number_v2(n)