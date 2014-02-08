total = input()
max_num = input()
less_num = [0, total - max_num*2][total - max_num*2 > 0]
print ["not surprising", "surprising"][max_num - less_num > 2]
