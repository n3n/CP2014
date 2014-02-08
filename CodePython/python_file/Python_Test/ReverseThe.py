#ls = str(raw_input()).split()
#for i in xrange(len(ls)):
	#if ':' in ls[i]:
		#ls[i] = ':'.join(ls[i].split(':')[::-1])
#print ' '.join(ls[::-1])

def cnt_space(text):
	ls = [0]
	cnt = 0
	for i in text:
		if i == ' ':
			cnt +=1
		elif cnt != 0:
			ls += [cnt]
			cnt = 0
	return ls

text = raw_input()
ls = text.split()
#print cnt_space(text)
ls_space = cnt_space(text)
for i in xrange(len(ls)-1,-1,-1):
	print ls[i] + ' '*(ls_space[i]-1),