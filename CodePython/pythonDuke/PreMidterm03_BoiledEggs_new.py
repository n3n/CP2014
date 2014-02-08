def most_eggs_in_pot(n_eggs, most_eggs, most_grams):
    total_grams = 0
    total_eggs  = 0
    ls_eggs = map(int, raw_input().split())
    ls_eggs.sort()
    i = 0
    while i < n_eggs :
        cur_gram = ls_eggs.pop(0)
        if total_grams+cur_gram > most_grams or \
           total_eggs >= most_eggs:
            break
        total_grams += cur_gram
        total_eggs += 1
        i += 1
    return total_eggs
        
for case in xrange(1,input()+1):
    ls = map(int, raw_input().split())
    print 'Case ' + str(case) + ': ' + str(most_eggs_in_pot(ls[0], ls[1], ls[2]))
