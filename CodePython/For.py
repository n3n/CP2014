for i in range(input()):
    n = input()
    if isinstance(n, list):
        for i in n:
            print i+2
    else:
        for i in n:
            print i*2
