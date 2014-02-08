m = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1,input()+1):
	n = 0
	name = raw_input()
	for j in name:
		n += (m.find(j)+1)
	print 'Name',i,':',n*i
