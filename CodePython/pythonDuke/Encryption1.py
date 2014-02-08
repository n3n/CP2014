def encryption(a, b, c):
    """
    encryption(a, b, c) -> str

    Return encode of a, b and c.
    """
    encode = ''
    for i in xrange(10):
        encode += str((a+i)%10 + (b+i)%10 + (c+i)%10)
    return encode

print encryption(*map(int, raw_input()))
