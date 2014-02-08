amout = input()
power_max = 0
i = 1
name = ''
while i <= amout:
	target, power = raw_input().split()
	if int(power) > power_max:
		power_max = int(power)
		name = target
	i += 1

print name