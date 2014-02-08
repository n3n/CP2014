dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
roman = raw_input().split()
s = ''
for j in roman:
	value = 0
	len_ro = len(j)
	for i in xrange(len_ro):
		if i+1 < len_ro and dic[j[i]] < dic[j[i+1]]:
			value -= dic[j[i]]
		else:
			value += dic[j[i]]
	s += chr(value)
print s

#LXXX XCVII CXV CXV CXIX CXI CXIV C XXXII CV CXV XXXII LVIII XXXII LXVI LXXVI LXXV LXXI LXX LXXXI LXV LXIX LXV LXVIII LXXII LXXXIV LXXXII LXXXIII LXXXVII LXX LXXXVI LXVIII LXXVIII LXVII XC LXVI LXVII LXXIV LXXX LXXXIX LXXXVIII LXXVII LXXXV LXIX 
