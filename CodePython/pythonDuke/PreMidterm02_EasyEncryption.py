st = raw_input()
st_out = ''
for ch in st:
    if ch >= 'A' and ch <= 'Z':
        st_out += str(ord(ch) - 64 + 26).zfill(2)
    elif ch >= 'a' and ch <= 'z':
        st_out += str(ord(ch) - 96).zfill(2)
    elif ch >= '0' and ch <= '9':
        st_out += '#' + ch
    else:
        st_out += ch
print st_out.strip()
        
