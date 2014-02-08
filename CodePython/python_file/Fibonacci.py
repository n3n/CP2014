n = input()
fibo=[0,1]
for i in range(2,n+1):
##    if n == 0:
##        print 0
##        break
##    elif n == 1:
##        print 1
##        break
    fibo.append(fibo[i-1]+fibo[i-2])
#print fibo[n-1]
print fibo[n]
