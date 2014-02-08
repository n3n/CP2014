def decoder(st):
    i = 0
    st_encode = ''
    for ch in st:
        if ch in string.ascii_letters:
            i = (i + 1)%26
            if ch.isupper():
                st_encode += string.ascii_uppercase[(string.ascii_uppercase.index(ch)+i) % 26]
            else:
                st_encode += string.ascii_lowercase[(string.ascii_lowercase.index(ch)+i) % 26]
        else:
            st_encode += ch
    return st_encode

import string
st = raw_input()
print decoder(st)
