alist = input()
maxValue = 0
gum = ''
for i in str(alist):
	if i == '[' or i == ']':
		gum += ''
	else:
		gum += i
gum = gum.split(',')
for j in gum:
	if int(j) > maxValue:
		maxValue = int(j)
print maxValue
