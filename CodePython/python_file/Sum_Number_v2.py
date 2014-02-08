n1 = input()
n2 = input()
def sum_number_v2(n1, n2):
    count = 0
    while n2 >= n1:
        count += n1
        n1 += 1
    print count
sum_number_v2(n1, n2)
