n = [int(i) for i in raw_input().split()]
cnt = 0
while n[0] != 1 or n[1] != 1 or n[2] != 1:
	max_value = max(n)
	if max_value%2 != 0:
			max_value -= 1
	max_value /= 2
	cnt += 1
	n[n.index(max(n))] = max_value

print cnt