message = raw_input()
list_Word = []

for index in xrange(len(message)-1):
    list_Word.append(message[index]+message[index+1])

max_Val = 0

for word in list_Word:
    if list_Word.count(word) > max_Val:
        max_Val = list_Word.count(word)

for word2 in list_Word:
    if list_Word.count(word2) == max_Val:
        print '%s\n%d' % (word2, max_Val)
        break
