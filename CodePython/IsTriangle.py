def is_Triangle(a,b,c):
    lenght = sorted([a,b,c])
    if (lenght[0]**2 + lenght[1]**2) == lenght[2]**2:
        return "Yes."
    return "No."

print is_Triangle(input(),input(),input())
