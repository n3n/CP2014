def QE(a,b,c):
    try:
        x1 = (-b + (((b**2) - (4*a*c))**0.5))/(2*a)
        x2 = (-b - (((b**2) - (4*a*c))**0.5))/(2*a)
        if x1==x2: return x2
    except:
        return "complex root"
    return '%.4f\n%.4f'%(min(x1,x2),max(x1,x2))
print QE(input(),input(),input())
