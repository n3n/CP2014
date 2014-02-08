st1 = raw_input()
st2 = raw_input()
if len(st1) > len(st2):
    buf = st1
    st1 = st2
    st2 = buf

st_same = ''
n_same = 0
for head in xrange(len(st1)):
    for tail in xrange(len(st1)):
        if st1[head:tail+1] in st2 and tail+1-head > n_same:
            st_same = st1[head:tail+1]
            n_same  = tail+1-head

if st_same == '':
    print 'Error!'
else:
    print st_same
