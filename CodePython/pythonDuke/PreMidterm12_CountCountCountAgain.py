letter = [chr(i+97) for i in xrange(26)]
letter += [str(i) for i in xrange(10)]
def isWord(text):
    for ch in text:
        if ch in letter:
            return True
    return False

n = input()
st = ''
for i in xrange(n):
    st += ' ' + raw_input()
ls = (st.lower()).split()

total_word = 0
for word in ls:
    if isWord(word):
        total_word += 1

print total_word
