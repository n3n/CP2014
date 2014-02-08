de,en = raw_input(), raw_input()
n = 0; cnt = 0
while n != len(de):
    m1 = (ord(de[n])-ord(en[n]))%26
    m2 = (ord(en[n])-ord(de[n]))%26
    if m1 > m2:
        cnt += m2
    else:
        cnt += m1
    n+= 1
print cnt