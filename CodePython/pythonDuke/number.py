num_thai = ['', '˹��', '�ͧ', '���', '���', '���', 'ˡ', '��', 'Ỵ', '���']
pref_num = ['', '', '����', '�ѹ', '����', '�ʹ', '��ҹ']

n = raw_input()
len_n = len(n)
st = ''
for i in xrange(0, len_n-2):
    st += num_thai[int(n[i])] + pref_num[(len_n-i-1)*(int(n[i])!=0)]

print st
