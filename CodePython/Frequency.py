def histogram(string):
    ''' string -> dictionary
    '''
    d = {}
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

def frequency(string):
    '''
        string -> string
        return ...
    '''
    alist = []
    frequency_str = histogram(string)
    max_Frequency = max(frequency_str.values())
    for i in frequency_str:
        if frequency_str[i] == max_Frequency:
            alist.append(i)
    alist.sort()
    return ' '.join(alist)

string = raw_input()
print frequency(string)
