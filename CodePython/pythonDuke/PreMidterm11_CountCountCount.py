st = ''
for i in xrange(input()):
    st += raw_input()
st = st.lower()

dic = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for ch in st:
    if ch in 'aeiou':
        dic[ch] += 1

for key in 'aeiou':
    print key+':', dic[key]

