dot_pos = [0 for i in xrange(10001)]
end_pos, Li, Hi, Ri = 0, 0, 0, 0
import time
for i in xrange(input()):
    Li, Hi, Ri = map(int, raw_input().split())
    end_pos = max(end_pos, Ri)
    for pos in xrange(Li, Ri):
        dot_pos[pos] = max(dot_pos[pos], Hi)
        print dot_pos[:pos]
    #time.sleep(5)
pos = 0
for j in xrange(1, end_pos+1):
    if pos != dot_pos[j]:
        print j, dot_pos[j],
        pos = dot_pos[j]

        
