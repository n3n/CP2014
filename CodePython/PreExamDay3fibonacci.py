f1 = 1
f2 = 1
cnt = 2
import time
n = input()
old = time.time()
while len(str(f2)) != n:
    cnt += 1
    f1, f2 = f2, f1 + f2
print cnt #time.time()-old
