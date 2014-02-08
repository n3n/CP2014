from math import *

def ceasar(text, shift):
	res = ''
	a = ord('a')
	A = ord('A')
	for i in text:
		code = ord(i)
		if i >= 'A' and i <= 'Z':
			code = A + (code-A+shift)%26
		elif i >= 'a' and i <= 'z':
			code = a + (code-a+shift)%26
		
		res += chr(code)

	return res

def len_fb(st):
	# gen new text.
	text = ''
	for i in st:
		if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
			text += i
		else:
			text += ' '

	ls = text.split()

	len_f = 0
	for i in ls[0]:#text:
		if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
			len_f += 1
		else:
			break

	len_b = 0
	for i in ls[-1]:#xrange(len(text)-1,-1,-1):
		if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'): #if (text[i] >= 'A' and text[i] <= 'Z') or (text[i] >= 'a' and text[i] <= 'z'):
			len_b += 1
		else:
			break

	return len_f, len_b

def is_prime(n):
	for i in xrange(2,n):
		if n%i==0:
			return False
	return True

def next_prime(n):
	n += 1
	while not is_prime(n):
		n += 1
	return n

text = raw_input()
len_f,len_b = len_fb(text)
#if len_f < len_b:
#	key	 = len_b
#	ls = (list(text.split()[-1])[-2:-len_b-2:-1])
#	ls.reverse()
#	buf_text = ''.join(ls)
#else:
#	key  = len_f
#	buf_text = text.split()[0]

#len_key  = len(text.split()[0])
key  = len(text.split()[0])

#if not is_prime(key):
#	key = next_prime(key)

key = key * -1

#print key, is_prime(1)
print ceasar(text, key)