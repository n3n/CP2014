n = input()
def sum_number_v1(n):
    count = 0
    while n >= 0:
        count += n
        n -= 1
    print count
sum_number_v1(n)
