word = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = ''
for i in word:
    if len(str(word.index(i))) == 1:
        message += "0" + str(word.index(i)) + 1
    elif len(str(word.index(i))) == 2:
        message += str(word.index(i)) + 1
