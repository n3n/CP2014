for amount in xrange(input()):
    special = input()
    normal = input()
    for order in xrange(input()):
        weight = input()
        price = input()
        if weight >= special:
            total = ((price * 10)/100.0) + price
            if total != int(total):
                print int(total+1)
            else:
                print int(total)
        elif normal <= weight < special:
            total = ((price * 20)/100.0) + price
            if total != int(total):
                print int(total+1)
            else:
                print int(total)
        else:
            print price
