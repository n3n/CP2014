wordlist = []
for vocab in xrange(input()):
    wordlist.append(raw_input())

def palindrome_2D(wordlist):
    if len(wordlist) % 2 == 0:
        for index in xorange(len(wordlist)/2):
            if wordlist[index] != wordlist[(len(wordlist)-1)-index][::-1]:
                return 'NO'
        return 'YES'
    else:
        for index in xrange((len(wordlist)/2)+1):
            if wordlist[index] != wordlist[(len(wordlist)-1)-index][::-1]:
                return 'NO'
        return 'YES'

print palindrome_2D(wordlist)
