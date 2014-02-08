def gcd(x,y):
    if y == 0:
        if x == 0:
            return 0
        else:
            return x
    elif x%y == 0:
        return y
    else:
        return gcd(y,x%y)

x, y = input(), input()
print gcd(max(x,y), min(x,y))
