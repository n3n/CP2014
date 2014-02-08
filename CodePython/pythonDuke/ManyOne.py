ls = [0,1,2]
i = 2
n = input()
if i > n:
    i = n
while i < n:
    ls.append(ls[i]+ls[i-1])
    i += 1
print '1'*ls[i]
