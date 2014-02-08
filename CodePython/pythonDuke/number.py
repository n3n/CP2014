num_thai = ['', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
pref_num = ['', '', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

n = raw_input()
len_n = len(n)
st = ''
for i in xrange(0, len_n-2):
    st += num_thai[int(n[i])] + pref_num[(len_n-i-1)*(int(n[i])!=0)]

print st
