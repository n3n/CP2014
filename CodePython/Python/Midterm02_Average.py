def thestrip(txt):
    ret = ''
    for let in txt:
        if let.isalpha():
             ret += let
    return ret

text = raw_input().split()
word = []
char = 0.0
count = 0.0
for each in text:
    tmp = thestrip(each)
    if len(tmp) > 0 and tmp.isalpha():
        char += len(tmp)
        count += 1

if count > 0:
    res = (char / count)
else:
    res = 0

print '%.2f' % res
