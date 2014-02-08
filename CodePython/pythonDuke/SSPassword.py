def stKey(st):
    if len(st[0]) < len(st[1]):
        return st[0], st[1]
    return st[1], st[0]

st = raw_input(), raw_input()
st1, st2 = stKey(st)

key = ''
max_len = 0;
for i_head in xrange(len(st1)):
    for i_rear in xrange(i_head, len(st1)):
        if st1[i_head:i_rear+1] in st2 and \
           i_rear - i_head + 1 > max_len:
               key = st1[i_head:i_rear+1]
               max_len = i_rear - i_head + 1
print key
