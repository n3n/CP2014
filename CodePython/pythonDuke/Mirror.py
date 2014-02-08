st = raw_input()
st_out = ''
for ch in st[::-1]:
    if ch == '(':
        st_out += ')'
    else:
        st_out += '('
print st_out
