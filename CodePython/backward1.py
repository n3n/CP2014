alist = []
def backward():
    string = raw_input()
    if string == 'NULL':
        print '\n'.join(alist)
        return 0
    alist.insert(0, string)
    backward()

backward()
