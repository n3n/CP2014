txt = raw_input()

txt = txt.replace(')','x')
txt = txt.replace('(',')')
txt = txt.replace('x','(')

print txt[::-1]