def myList_reverse(ls):
    ls.reverse()
    for i in ls:
        if isinstance(i, list):
            myList_reverse(i)

myList = input()
myList_reverse(myList)
print myList
