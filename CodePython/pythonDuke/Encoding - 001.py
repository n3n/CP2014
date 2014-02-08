st = raw_input()
st_out = ''
encode = ['A', 'a']
i = 0
for ch in st:
    if ch.upper() == 'A' or \
       ch.upper() == 'E' or \
       ch.upper() == 'I' or \
       ch.upper() == 'O' or \
       ch.upper() == 'U' :
        st_out += encode[i%2]
    else:
        st_out += ch
    i += 1
print st_out
       
