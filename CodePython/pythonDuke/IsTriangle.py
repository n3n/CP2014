def isTriangle(a,b,c):
    triangle = sorted([a,b,c])
    if not triangle[2]**2 == triangle[1]**2 + triangle[0]**2 or \
    a < 1 or b < 1 or c < 1:
        return False
    return True

print ['No.', 'Yes.'][isTriangle(input(),input(),input())]
