line1, line2, summary, i = [], [], 0, 0
line1.extend(raw_input())
line2.extend(raw_input())
if len(line1) > len(line2):
	while len(line2) != len(line1):
		line2.insert(0,0)
elif len(line2) > len(line1):
	while len(line2) != len(line1):
		line1.insert(0,0)	
while i < len(line1):
	summary += (int(line1[i])*int(line2[i]))
	i += 1
print summary
