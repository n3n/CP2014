txt1 = raw_input()
txt2 = raw_input()
 
start = 0
store = {}
 
for j in xrange(len(txt2)):
    tmp = ''
    for i in xrange(1,len(txt2)+1):
        if txt2[j:i] in txt1:
            tmp = txt2[j:i]
    if len(tmp) > 0:
        store[tmp] = len(tmp)
 
val = store.values()
val.sort()
if len(val) == 0:
    print 'Error!'
else:
    for x in store:
        if store[x] == val[-1]:
            print x
            break
