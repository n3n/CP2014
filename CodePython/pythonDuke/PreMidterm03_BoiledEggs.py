def most_eggs_in_pot(n_eggs, most_eggs, most_grams):
    cur_eggs = []
    ls_eggs  = map(int, raw_input().split())
    maximal  = [0 for i in xrange(most_grams+1)]
    for i in xrange(n_eggs):
        cur_eggs.append(ls_eggs[i])
        maximal[ls_eggs[i]] = 1
    n_cur = n_eggs
    while n_cur > 0:
        cur = cur_eggs.pop(0)
        n_cur -= 1
        for egg in ls_eggs:
            if egg+cur <= most_grams                            and \
               maximal[egg+cur] < maximal[cur] + maximal[egg]   and \
               maximal[cur] + maximal[egg] <= most_eggs:
                maximal[egg+cur] = maximal[cur] + maximal[egg]
                cur_eggs.append(egg+cur)
                n_cur += 1
    return max(maximal)

ls = map(int, raw_input().split())
print most_eggs_in_pot(ls[0], ls[1], ls[2])
