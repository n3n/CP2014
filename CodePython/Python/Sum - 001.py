total = 0
i = 0
while True:
	temp = input()
	if temp == -1:
		break
	else:
		total += temp
		i += 1

print total / i