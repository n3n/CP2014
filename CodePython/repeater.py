try:
    string = raw_input()
    length = len(string)-1
    for index in xrange(len(string)):
        print ' '*((length)*2)+' '.join(list(string[::-1][length:len(string)-1] + string[:index+1]))
        length -= 1       
except:
    print ''
