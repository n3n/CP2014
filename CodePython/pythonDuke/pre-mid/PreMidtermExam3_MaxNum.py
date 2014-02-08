st = raw_input()
ls = st.split('[')
st = ''.join(ls)

ls = st.split(']')
st = ''.join(ls)

ls = st.split(',')
ls = map(int, ls)
print max(ls)
