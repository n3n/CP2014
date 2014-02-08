num1 = map(int, raw_input())
num2 = map(int, raw_input())
min_len = min(len(num1), len(num2))
total = 0
i = 0
while i < min_len:
    total += num1[-1-i]*num2[-1-i]
    i+=1
print total
