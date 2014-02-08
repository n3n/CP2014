string = raw_input()
try:
    d = {}
    for index in xrange(len(string)):
        if string[index] + string[index+1] not in d:
            d[string[index] + string[index+1]] = 1
        else:
            d[string[index] + string[index+1]] += 1
except:
    pass
li = []
for key in d:
    if d[key] == max(d.values()):
        li.append(key)
try:
    for i in xrange(len(string)):
        if string[i] + string[i+1] in li:
            print "%s\n%d" % (string[i]+string[i+1],max(d.values()))
            break
except:
    pass
 
