n = input()
for i in xrange(1,n+1):
    st_out = ' ' *  (n-i)
    for j in xrange(i*2-1):
        if j == 0 or j == i*2-2:
            st_out += '1'
        else:
            st_out += '0'
    print st_out
