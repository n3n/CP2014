for i in xrange(input()):
    oil = input()
    money = input()
    print int(money/oil)
    print int(money - (int(money/oil) * oil))
