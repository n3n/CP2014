def BookWorm():
    for i in xrange(input()):
        time_for_read = input()
        books = []
        for time in xrange(input()):
            books.append(input())
        count, times, ok = 0, 0, True
        for book in sorted(books):
            times += book
            count += 1
            if times > time_for_read:
                ok = False
                print count-1
                break
        if ok: print count
BookWorm()
        
