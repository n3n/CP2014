import string
def check(s):
    d = {}
    for i in s:
        if i.lower() in string.lowercase:
            if i.lower() not in d:
                d[i.lower()] = 1
            else:
                d[i.lower()] += 1
    return d

def dict_v2(s):
    #d = check(s)
    dict2 = {}
    for i in s:
        if s[i] not in dict2:
            dict2[s[i]] = [i]
        else:
            dict2[s[i]].append(i)
    return dict2
print dict_v2(input())
