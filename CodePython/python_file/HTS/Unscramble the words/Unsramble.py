import time
mine = time.time()
wordlist,alist = [],[]
for w in open("list.txt"):
    wordlist.append(w.strip())
for word in wordlist:
    for i in open("wordlist.txt"):
        cnt = 0
        if len(word) == len(i.rstrip()):
            for j in i.strip():      
                if j in word and word.count(j) == i.strip().count(j):
                    cnt += 1
                    if cnt == len(i.strip()):
                        alist.append(i.strip())
                        break
                elif j not in word:
                    break

print ','.join(alist)
print time.time() - mine,"sec."

