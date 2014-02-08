dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
roman = raw_input()
value = 0
len_ro = len(roman)
for i in xrange(len_ro):
	if i+1 < len_ro and dic[roman[i]] < dic[roman[i+1]]:
		value -= dic[roman[i]]
	else:
		value += dic[roman[i]]
print value
