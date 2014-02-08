def decrementor(ls, n):
    for i in xrange(n):
        ls[i] -= 1

total_day = 0
n = input()
ls = map(int,raw_input().split())
ls.sort(reverse=True)
min_num = ls.pop(-1)

while min_num > 0:
    decrementor(ls, n-1)
    ls.append(min_num)
    if min_num > ls[-2]:
        ls.sort(reverse=True)  
    min_num = ls.pop(-1)
    total_day += 1
    #print ls, min_num

print total_day
