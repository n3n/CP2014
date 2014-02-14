alldist = float(input())
player = input()
alltime = []
for each in xrange(player):
    data = raw_input().split()
    alltime.append((alldist - int(data[1])) / int(data[0]))
print alltime.index(min(alltime)) + 1
