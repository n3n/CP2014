def manga(alist):
    emptylist = []
    for i in alist[::-1]:
        if type(i) == list:
            emptylist.append(manga(i))
        else:
            emptylist.append(i)
    return emptylist
print manga(input())
