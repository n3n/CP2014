line1, line2, line3 = [], [], []
for i in raw_input():
	line1.append(i)
for j in raw_input():
	line2.append(j)
for k in raw_input():
	line3.append(k)
chk, chk2, chk3, chk4 = '','','',''

for i in ''.join(line1),''.join(line2),''.join(line3):	
	try:
		if i == 'XXX' or i == 'OOO':
			print i[0]+" -"
			break
		elif i[0] == 'X' or i[0] == 'O':
			chk += i[0]
			if chk == 'OOO' or chk == 'XXX':
				print chk[0] + " |"
				break
		elif i[1] == 'X' or i[1] == 'O':
			chk3 += i[1]
			if chk3 == 'OOO' or chk3 == 'XXX':
				print chk3[1] + " |"
				break
				
		elif i[2] == 'X' or i[2] == 'O':
			chk4 += i[2]
			if chk4 == 'OOO' or chk4 == 'XXX':
				print chk4[2] + " |"
				break
				
		if i[0] == 'X' or i[0] == 'O':
			chk2 += i[0]
			continue
		elif i[1] == 'X' or i[1] == 'O':
			chk2 += i[1]
			continue
		elif i[2] == 'X' or i[2] == 'O':
			print chk2[0] + ' \\'

		if i[2] == 'X' or i[2] == 'O':
			chk2 += i[2]
			continue
		elif i[1] == 'X' or i[1] == 'O':
			chk2 += i[1]
			continue
		elif i[0] == 'X' or i[0] == 'O':
			print chk2[0] + ' /'
	except:
		pass

		
		
		
