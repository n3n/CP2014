for i in xrange(input()):
    vowel_lower = 'uoiea'
    vowel_upper = 'UOIEA'
    interpreter = ''
    for word in raw_input():
        if word in vowel_lower:
            interpreter += vowel_lower[vowel_lower.index(word)-1]
        elif word in vowel_upper:
            interpreter += vowel_upper[vowel_upper.index(word)-1]
        else:
            interpreter += word
    print interpreter
